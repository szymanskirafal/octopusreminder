from django.forms import CheckboxInput, ModelForm, Textarea
from .models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['text', 'today']
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
            'today': CheckboxInput(
                attrs={
                    'class': 'form-check-input',

                }
            ),
        }
