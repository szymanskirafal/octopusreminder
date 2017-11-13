from django.forms import ModelForm, Textarea
from .models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['text']
        labels = {
            'text': '',
        }
        widgets = {
            'text': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': ' type here...',
                    'autofocus': '',

                }
            ),
        }
