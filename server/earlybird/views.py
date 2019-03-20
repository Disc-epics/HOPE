from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model

from .models import Client, PendingUsers
from .forms import SignupForm
from .send_email import send_email

import uuid
import random

User = get_user_model()


@login_required
def acct_page(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


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
