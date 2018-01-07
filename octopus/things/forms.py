from django.forms import CheckboxInput, ModelForm, Textarea
from .models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['text', 'today']
        labels = {
            'text': '',
            'today': 'Today',

        }
        widgets = {
            'text': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': ' type here...',
                    'autofocus': '',

                }
            ),
            'today': CheckboxInput(
                attrs={
                    'class': 'btn btn-secondary',

                }
            ),
        }
