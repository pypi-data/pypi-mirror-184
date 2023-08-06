from django.test import TestCase
from games.models import GameSystem


class GameSystemTestCase(TestCase):
    def setUp(self):
        GameSystem.objects.create(name="System with No Color")
        GameSystem.objects.create(name="System with Custom Color", color="AACCAA")
        GameSystem.objects.create(name="System with Default Color", retropie_slug="fds")
        GameSystem.objects.create(
            name="System with Default Color and Override",
            color="000000",
            retropie_slug="fds",
        )

    def test_get_color(self):
        no_color = GameSystem.objects.get(name="System with No Color")
        custom_color = GameSystem.objects.get(name="System with Custom Color")
        default_color = GameSystem.objects.get(name="System with Default Color")
        overriden_color = GameSystem.objects.get(
            name="System with Default Color and Override"
        )

        self.assertEqual(None, no_color.get_color)
        self.assertEqual("AACCAA", custom_color.get_color)
        self.assertEqual("B70E30", default_color.get_color)
        self.assertEqual("000000", overriden_color.get_color)
