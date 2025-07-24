from django.test import TestCase

from .models import Song
from .constants import KEY_OPTIONS


class SongModelTest(TestCase):
    def test_key_choices(self):
        field = Song._meta.get_field("key")
        self.assertEqual(field.choices, KEY_OPTIONS)
