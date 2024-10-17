from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('list.html', views.PropertyListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.PropertyDetailView.as_view(), name='detail'),
     path('new/', views.PropertyCreateView.as_view(), name='create'),
    
]
