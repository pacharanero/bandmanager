"""bandmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from bandapp.views import (
    index,
    sandbox,
    SetlistListView,
    SetlistDetailView,
    SignUpView,
    SongListView,
    copy_setlist,
    add_song_to_setlist,
    )

admin.site.site_header = "Band Manager"
admin.site.site_title = "Band Manager Portal"
admin.site.index_title = "Welcome to Band Manager"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('setlists/<uuid:pk>/copy/', copy_setlist, name="setlist-copy"),
    path('setlists/<uuid:pk>/add-song/', add_song_to_setlist, name='setlist-add-song'),
    path('setlists/<uuid:pk>/', SetlistDetailView.as_view(), name='setlist-detail'),
    path('setlists/', SetlistListView.as_view(), name="setlist-list"),
    path('songs/', SongListView.as_view(), name="song-list"),
    path('gigs/', SetlistListView.as_view(), name="setlist-list"),
    path('sandbox/', sandbox, name = 'sandbox'),
    path('', index, name="index"),
]
