from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

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
