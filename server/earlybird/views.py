from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model
from django.http import JsonResponse
from django.contrib.auth import logout
from django.conf import settings

from .models import Client, PendingUsers
from .forms import SignupForm, AddClient
from .send_email import send_email

import uuid
import random

User = get_user_model()

def logout_view(request):
    logout(request)
    # Redirect to a success page
    return redirect('{}/'.format(settings.PREFIX))

@login_required
def acct_page(request):
    client_list = ['{} {}'.format(c.first_name, c.last_name)
                   for c in request.user.client_set.all()]
    return render(request, 'client_list.html', {'clients': client_list, 'username': request.user.username})


@login_required
def get_status(request, client_name):
    # Assuming NO MIDDLE NAMES for now
    first_name = client_name.split()[0]
    last_name = client_name.split()[1]
    client = request.user.client_set.get(
        first_name=first_name, last_name=last_name)

    data = {
        'status': client.status
    }
    return JsonResponse(data)


def register_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            # generate a UUID to be in the email
            key = str(uuid.uuid4())
            pending_user = PendingUsers(
                email=email, first_name=first_name, last_name=last_name, key=key)
            pending_user.save()

            send_email('russellgreene8@gmail.com', 'Is good?',
                       'Is good? {0} with email {1} <br /> <a href={2}>{2}</a>'.format(first_name, email, "http://localhost:8000/confirm/{}".format(key)))

            return render(request, 'request_received.html')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})


@login_required
def client_page(request):
    if request.method == 'POST':
        form = AddClient(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            middle_name = form.cleaned_data.get('middle_name')
            user = request.user
            pending_client = Client(
                first_name=first_name, last_name=last_name, middle_name=middle_name, user=user
            )
            pending_client.save()
            # need to make html for adding client
            # return render(request, 'client_created.html')
            return redirect('/account/')
    else:
        form = AddClient()
    return render(request, 'add_client.html', {'form': form})


def confirm_user(request, uuid=None):
    pending_user = PendingUsers.objects.get(key=uuid)
    if pending_user:
        # give them a password
        password_chars = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
        password = ''.join(random.sample(password_chars, 8))

        # create the user
        new_user = User.objects.create_user(first_name=pending_user.first_name,
                                            last_name=pending_user.last_name,
                                            username=pending_user.email,
                                            email=pending_user.email, password=password)

        new_user.save()

        # email the new user
        send_email(pending_user.email, 'Your earlybird account has been activated!',
                   'Your password is {}'.format(password))

        return render(request, 'user_created.html', {
            'name': '{} {}'.format(pending_user.first_name, pending_user.last_name),
            'email': pending_user.email,
        })
