from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Ticket
from .forms import TicketForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# def home(request: HttpRequest) -> HttpResponse:
#     return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')


def add_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets_list')
    else:
        form = TicketForm()
    return render(request, 'add_ticket.html', {'form': form})

# def tickets_list(request):
#     tickets = Ticket.objects.all().order_by('-creation_date')
#     return render(request, 'tickets_list.html', {'tickets': tickets})
# views.py
def tickets_list(request):
    tickets = Ticket.objects.exclude(status='resolved').order_by('-creation_date')
    return render(request, 'tickets_list.html', {'tickets': tickets})




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect(reverse('login_view'))  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('add_ticket'))  
    return render(request, 'login.html', {})
