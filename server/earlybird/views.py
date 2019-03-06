from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Client


@login_required
def acct_page(request):
    clients = Client.objects
    return render(request, 'client_list.html', {'clients': clients})
