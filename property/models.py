from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.conf import settings




# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(verbose_name='Property Price')
    description = models.TextField (verbose_name='Property Details')
    location = models.CharField (max_length=200,verbose_name='Property Location')
    date_added = models.DateField(default=timezone.now, verbose_name='Date Registered')
    availability = models.BooleanField(default=True)
    bedrooms = models.IntegerField(default=0, verbose_name='Number of bedrooms')

    class Meta:
        verbose_name_plural = 'Properties'
        ordering = ['name', 'price']
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('property:detail', kwargs={'pk:self.pk'})
    