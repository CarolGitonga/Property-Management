from django import forms

class PropertForm(forms.ModelForm):
    class Meta:
        exclude = ('date_added')
