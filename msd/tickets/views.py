from django.shortcuts import render, get_object_or_404, redirect

from .models import Tickets, Category
from .forms import TicketForm


def index(request):
    tickets = Tickets.objects.order_by('-created_at')
    context = {
        'tickets': tickets,
        'title': 'Список заявок',
    }
    return render(request, 'tickets/index.html', context)


def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'tickets/add_ticket.html', {'form': form})
