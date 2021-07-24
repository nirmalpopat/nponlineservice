from django.core import validators
from django import forms
from django.forms import widgets
from .models import Sells

class SellsForm(forms.ModelForm):
    agents = (('avesh','Avesh'),('ajay','Ajay'))
    items = (
        ('sim','SIM'),
        ('recharge','Recharge'),
        ('adhar_widrawal','Adhar Widrawal'),
        ('earphone','Ear-Phone'),
        ('money_transfer','Money Transfer'),
        ('neckband','Neckband'),
        ('charger','Charger'),
    )
    agent_name = forms.ChoiceField(choices = agents, widget = forms.RadioSelect)
    item_name = forms.ChoiceField(choices = items, widget = forms.RadioSelect)
    class Meta:
        model = Sells
        fields = ['agent_name','item_name','price','comment']
        widgets = {
            'agent_name' : forms.TextInput(attrs={'class':'form-control'}),
            'item_name' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'comment' : forms.TextInput(attrs={'class':'form-control'}),
        }