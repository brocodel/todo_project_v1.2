from .models import Deals
from .models import Dealer
from django.forms import ModelForm, TextInput, NumberInput, DateInput

class DealsForm(ModelForm):
    class Meta:
        model = Deals
        fields = ['text', 'priority', 'date']

        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control'
            }),
            'priority': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1-20'
            }),
            'date': DateInput(attrs={
                'class': 'form-contor',
                'placeholder': 'yyyy-mm-dd'
            })

        }


class DealerForm(ModelForm):
    class Meta:
        model = Dealer
        fields = ['login', 'password']

        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'login'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            })
        }