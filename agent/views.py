from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Agent
from .forms import AgentCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

# Create your views here.
class AgentListView(ListView):
    model = Agent

class AgentUpdateView(UpdateView) :
    model = Agent
    template_name_suffix = 'update_form'
    fields = ('telephone', 'picture', 'description', 'address')

class AgentDetailView(DetailView) :
    model = Agent

class AgentCreateView(FormView):
    template_name = 'agent/agent_create_form.html'
    form_class = AgentCreationForm
    success_url = reverse_lazy('agent:success_create')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def success_agent_create(request):
    return render(request, 'agent/success_agent_create.html')