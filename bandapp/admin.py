from django.contrib import admin

from .models import (
    Band,
    Gig,
    Setlist,
    Song,
    Tag,
)


class BandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'phone',
        'description',
    )


class GigAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'date',
        'description',
    )


class SongInline(admin.TabularInline):
    model = Setlist.songs.through
    extra = 3


class SetlistAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    inlines = [
        SongInline,
    ]


class SongAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'original_artist',
        'tempo',
        'key',
        'notes',
        'chart_url',
        'video_url',
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'colour',
    )


admin.site.register(Setlist, SetlistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Gig, GigAdmin)
