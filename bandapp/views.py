from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Setlist, Song, Gig


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