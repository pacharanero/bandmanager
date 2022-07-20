from django.contrib import admin

from .models import Setlist, Song, Band


class SongInline(admin.TabularInline):
    model = Setlist.songs.through
    extra = 3



class SetlistAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [
        SongInline,
    ]


admin.site.register(Setlist, SetlistAdmin)
admin.site.register(Song)
admin.site.register(Band)
