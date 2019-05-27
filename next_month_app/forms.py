from django.forms import ModelForm, TextInput
from .models import Archive

class BookForm(ModelForm):
   class Meta:
       model = Archive
       fields = ['name']
       widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Axtar...'})}