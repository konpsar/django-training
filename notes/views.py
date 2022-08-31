from calendar import c
from typing import List
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Notes
from .forms import NotesForm
# Create your views here.

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    
    
def detail(request, pk):
    try:        
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
