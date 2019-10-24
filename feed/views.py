from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
)
from .models import Event

# Create your views here.
"""def index(request):
    events = Event.objects.all()[:10]

    context = {
        'events' : events
    }

    return render(request, 'feed/index.html', context)"""

class EventListView(ListView):
    model = Event
    template_name = 'feed/index.html'
    context_object_name = 'events'
    ordering = ['-created_at']

def details(request, id):
    event = Event.objects.get(id=id)

    context = {
        'event': event 
    }

    return render(request, 'feed/details.html', context)

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'amount', 'members', 'created_at', 'end_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Event
    fields = ['title', 'description', 'amount', 'members', 'created_at', 'end_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    """def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False"""