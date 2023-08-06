from django.http import Http404
from activitypub.signatures import Signature
import json
import logging
import re

from django.core.exceptions import BadRequest, PermissionDenied
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from activitypub.exceptions import (
    BannedOrDeletedActorException,
    BlockedActorException,
    BlockedUserAgentException,
)

from activitypub.models import FederatedServer

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
# pylint: disable=no-self-use
class InboxView(View):
    """requests sent by outside servers"""

    def post(self, request, username=None):
        """InboxView handles requests sent from outside our instance"""
        self.check_is_blocked_user_agent()

        # make sure the user's inbox even exists
        if username:
            get_object_or_404(User, localname=username, is_active=True)

        # is it valid json? does it at least vaguely resemble an activity?
        try:
            activity_json = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            raise BadRequest()

        # let's be extra sure we didn't block this domain
        self.check_is_blocked_activity(activity_json)

        if (
            not "object" in activity_json
            or not "type" in activity_json
            or not activity_json["type"] in activitypub.activity_objects
        ):
            raise Http404()

        # verify the signature
        if not has_valid_signature(request, activity_json):
            if activity_json["type"] == "Delete":
                # Pretend that unauth'd deletes succeed. Auth may be failing
                # because the resource or owner of the resource might have
                # been deleted.
                return HttpResponse()
            return HttpResponse(status=401)

        activity_task.delay(activity_json)
        return HttpResponse()

    def check_is_blocked_user_agent(self) -> None:
        """Raise an exception if a request is from a blocked server based on user agent"""

        user_agent = self.request.headers.get("User-Agent")
        if not user_agent:
            return
        url = re.search(rf"https?://{regex.DOMAIN}/?", user_agent)
        if not url:
            return
        url = url.group()
        if FederatedServer.is_blocked(url):
            logger.debug(
                "%s is blocked, denying request based on user agent", url
            )
            raise BlockedUserAgentException

    def check_is_blocked_activity(self, activity_json: dict) -> None:
        """Raise an exception if actor of an activity is blocked"""
        actor = activity_json.get("actor")

        if not actor:
            return

        # TODO Remove User hard-code and add an AP Profile
        existing = User.find_existing_by_remote_id(actor)
        if existing:
            if existing.deleted:
                logger.debug("%s is banned/deleted", actor)
                raise BannedOrDeletedActorException
            if existing.banned:
                logger.debug("%s is banned/deleted", actor)
                raise BannedOrDeletedActorException

        if FederatedServer.is_blocked(actor):
            logger.debug("%s is blocked", actor)
            raise BlockedActorException

    def is_signature_valid(self, activity) -> bool:
        try:
            signature = Signature.parse(self.request.headers["Signature"])

            key_actor = urldefrag(signature.key_id).url
            if key_actor != activity.get("actor"):
                raise ValueError("Wrong actor created signature.")

            remote_user = resolve_remote_id(key_actor, model=User)
            if not remote_user:
                return False

            try:
                signature.verify(remote_user.key_pair.public_key, self.request)
            except ValueError:
                old_key = remote_user.key_pair.public_key
                remote_user = resolve_remote_id(
                    remote_user.remote_id, model=models.User, refresh=True
                )
                if remote_user.key_pair.public_key == old_key:
                    raise  # Key unchanged.
                signature.verify(remote_user.key_pair.public_key, self.request)
        except (ValueError, requests.exceptions.HTTPError):
            return False
        return True
