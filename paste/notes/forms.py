from django.forms import ModelForm
from .models import Notes
# Create the form class.


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'body', 'addresee']
