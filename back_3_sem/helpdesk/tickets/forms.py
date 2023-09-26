from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'phone', 'email', 'description', 'priority']
   

class ActionForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['action', 'status']
