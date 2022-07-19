from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Setlist



class SetlistListView(ListView):
    model = Setlist
    paginate_by = 100  # if pagination is desired

