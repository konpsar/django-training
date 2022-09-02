from calendar import c
from typing import List
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import NotesForm
from .models import Notes
# Create your views here.

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"
    
    #Search on ccbv.co.uk/projects/Django/3.1/ to get help on class views and find what 
    #we should alter in order to get only specific user's notes

    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    
    
def detail(request, pk):
    try:        
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
