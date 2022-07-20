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

from bandapp.views import SetlistListView, SongListView, index

admin.site.site_header = "Band Manager"
admin.site.site_title = "Band Manager Portal"
admin.site.index_title = "Welcome to Band Manager"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('setlists/', SetlistListView.as_view(), name="setlist-list"),
    path('songs/', SongListView.as_view(), name="song-list"),
    path('', index, name="index"),
]
