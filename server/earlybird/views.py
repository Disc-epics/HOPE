from django.shortcuts import render

from .models import Client


def acct_page(request):
    clients = Client.objects
    return render(request, 'acct_page.html', {'clients': clients})
