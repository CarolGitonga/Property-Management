from django.contrib import admin
from .models import BuildingType, Property, SaleType

# Register your models here.
admin.site.register(Property)
admin.site.register(SaleType)
admin.site.register(BuildingType)
