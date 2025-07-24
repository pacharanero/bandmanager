from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .models import (
    Band,
    Gig,
    Setlist,
    Song,
    Tag,
)


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {}
    return render(request, 'bandapp/index.html', context)


class SetlistListView(ListView):
    model = Setlist
    paginate_by = 20


class SongListView(ListView):
    model = Song
    paginate_by = 20


class GigListView(ListView):
    model = Gig
    paginate_by = 20


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def sandbox(request):
    context = {}
    return render(request, 'bandapp/sandbox.html', context)


def copy_setlist(request, pk):
    """Duplicate a setlist and redirect to the setlist list."""
    setlist = get_object_or_404(Setlist, pk=pk)
    setlist.copy()
    return redirect('setlist-list')


class SetlistDetailView(DetailView):
    """Display a single setlist with its songs."""
    model = Setlist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = Song.objects.all()
        return context


@require_POST
def add_song_to_setlist(request, pk):
    """Add a song to a setlist via AJAX."""
    setlist = get_object_or_404(Setlist, pk=pk)
    song_id = request.POST.get("song_id")
    song = get_object_or_404(Song, pk=song_id)
    setlist.songs.add(song)
    return JsonResponse({"status": "ok"})
