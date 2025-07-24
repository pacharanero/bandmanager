from django.test import TestCase
from django.conf import settings

from django.urls import reverse

from .models import Song, Setlist, Tag
from .constants import KEY_OPTIONS


settings.DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


class SongModelTest(TestCase):
    def test_key_choices(self):
        field = Song._meta.get_field("key")
        self.assertEqual(field.choices, KEY_OPTIONS)


class SetlistCopyTest(TestCase):
    def setUp(self):
        self.song1 = Song.objects.create(title="Song 1")
        self.song2 = Song.objects.create(title="Song 2")
        self.tag = Tag.objects.create(text="rock")
        self.setlist = Setlist.objects.create(title="My Set", description="d")
        self.setlist.songs.set([self.song1, self.song2])
        self.setlist.tags.add(self.tag)

    def test_copy_method(self):
        new_setlist = self.setlist.copy()
        self.assertEqual(new_setlist.title, "My Set (Copy)")
        self.assertQuerySetEqual(
            new_setlist.songs.order_by("id"),
            list(self.setlist.songs.order_by("id")),
            ordered=True,
        )
        self.assertQuerySetEqual(
            new_setlist.tags.order_by("id"),
            list(self.setlist.tags.order_by("id")),
            ordered=True,
        )

    def test_copy_view(self):
        response = self.client.get(reverse("setlist-copy", args=[self.setlist.pk]))
        self.assertRedirects(response, reverse("setlist-list"))
        self.assertEqual(Setlist.objects.count(), 2)


class AddSongToSetlistTest(TestCase):
    def setUp(self):
        self.song1 = Song.objects.create(title="Song 1")
        self.setlist = Setlist.objects.create(title="My Set")

    def test_add_song_view(self):
        url = reverse("setlist-add-song", args=[self.setlist.pk])
        response = self.client.post(url, {"song_id": self.song1.pk})
        self.assertEqual(response.status_code, 200)
        self.setlist.refresh_from_db()
        self.assertIn(self.song1, self.setlist.songs.all())
