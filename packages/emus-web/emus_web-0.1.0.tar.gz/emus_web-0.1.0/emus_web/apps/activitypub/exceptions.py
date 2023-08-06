class BlockedUserAgentException(Exception):
    pass


class DeletedActorException(Exception):
    pass


class BannedActorException(Exception):
    pass


class BlockedActorException(Exception):
    pass

class BannedOrDeletedActorException(Exception):
    pass
