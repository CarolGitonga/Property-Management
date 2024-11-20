from django.shortcuts import render
from .models import Property
from django.views.generic import DetailView,ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    paginate_by = 10
    extra_context  = {
        'hot_property_list': hot_properties(4)
    }
    def get_queryset(self):
        name = self.request.GET.get("name")
        building_type = self.request.GET.get("building_type")
        sale_type = self.request.GET.get("sale_type")
        min_price = self.request.GET.get("min")
        max_price = self.request.GET.get("max")

        property_list = Property.objects.all()
        if name is not None:
            property_list = property_list.filter(name__icontains=name)
        if sale_type is not None :
            property_list = property_list.filter(sale_type=sale_type)
        if building_type is not None:
            property_list = property_list.filter(building_type=building_type)
        if min_price is not None and min_price is not "":
            property_list = property_list.filter(price__gte=float(min_price))
        if max_price is not None and max_price is not "":
            property_list = property_list.filter(price__lte=float(max_price))
        return property_list
    
class PropertyCreateView(CreateView, LoginRequiredMixin):
    template_name_suffix = '_create_form'
    model = Property
    fields = (
        'name', 'price', 'location', 'description', 'building_type', 'sale_type', 'bedrooms',
        'bathrooms', \
        'picture_1', 'picture_2', 'picture_3', 'picture_4')
    
class PropertyDeleteView(DeleteView):
    model = Property

class PropertyUpdateView(UpdateView):
    template_name_suffix = '_update_form'
    model = Property
    fields = (
        'name', 'price', 'description', 'location', 'building_type', 'sale_type', 'bedrooms',
        'bathrooms', \
        'picture_1', 'picture_2', 'picture_3', 'picture_4')
    
    
    
        

