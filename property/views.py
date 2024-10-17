from django.shortcuts import render
from .models import Property
from django.views.generic import DetailView,ListView, CreateView

# Create your views here.
def hot_properties(number):
    property_list = Property.objects.filter(availability=True) [:number]
    return property_list

class PropertyDetailView(DetailView):
    model = Property
    extra_context  = {
        'hot_property_list': hot_properties(4)
    }
class PropertyListView(ListView):
    model = Property
    extra_context  = {
        'hot_property_list': hot_properties(4)
    }
class PropertyCreateView(CreateView):
    template_name_suffix = '_create_form'
    model = Property
    fields = (
        'name', 'price', 'location', 'description', 'bedrooms'
    )

