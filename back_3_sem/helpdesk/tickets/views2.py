# views.py
from .forms import TicketForm, ActionForm 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.core.exceptions import ObjectDoesNotExist
from .forms import ActionForm

def ticket_detail(request, ticket_id):
    try:
        ticket = Ticket.objects.get(pk=ticket_id)
    except ObjectDoesNotExist:
        # В зависимости от вашего приложения, вы можете выбрать другое перенаправление или действие.
        return redirect('tickets_list')
    
    if request.method == "POST":
        form = ActionForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets_list')
    else:
        form = ActionForm(instance=ticket)
    return render(request, 'ticket_detail.html', {'form': form, 'ticket': ticket})

