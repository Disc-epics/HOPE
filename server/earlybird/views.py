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
    if request.method == 'DELETE':
	request.user.delete()
        return redirect(settings.PREFIX)
    client_list = ['{} {}'.format(c.first_name, c.last_name)
		   for c in request.user.client_set.all()]
    client_list.sort(key=lambda x: x.split(" ")[-1])  # sorting by last names
    return render(request, 'client_list.html', {'clients': client_list, 'username': request.user.username, 'prefix': settings.PREFIX, 'snooping': False})


@login_required
def master_snoop(request, email):
    user = User.objects.get(email=email)
    client_list = ['{} {}'.format(c.first_name, c.last_name)
                   for c in user.client_set.all()]
    client_list.sort(key=lambda x: x.split(" ")[-1])  # sorting by last names
    return render(request, 'client_list.html', {'clients': client_list, 'username': request.user.username, 'prefix': settings.PREFIX, 'snooping': True})


@login_required
def master_page(request):
    user_list = [('{} {}'.format(u.first_name, u.last_name), u.email)
                 for u in User.objects.all()]
    return render(request, 'dashboard_master.html', {'users': user_list})


@login_required
def get_status(request, client_name):
    # Assuming NO MIDDLE NAMES for now
    first_name = client_name.split()[0]
    last_name = client_name.split()[1]
    client = Client.objects.get(
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
            phone_number = form.cleaned_data.get('phone_number')

            # generate a UUID to be in the email
            key = str(uuid.uuid4())
            pending_user = PendingUsers(
                email=email, first_name=first_name, last_name=last_name, phone_number=phone_number, key=key)
            pending_user.save()

            send_email('russellgreene8@gmail.com', 'Confirm registration for {} {}'.format(first_name, last_name),
                       'User {first} {last} ({email}) has requested access to earlybird. <br />'
                       'If you do not recognize this potential user, no action is required. If you would like to activate thier account, click the link below. <br /><br />'
                       '<a href={url}>{url}</a>'.format(first=first_name, last=last_name, email=email, url="http://engineering.purdue.edu/earlybirdsystem/confirm/{}".format(key)))

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
            return redirect('{}/account/'.format(settings.PREFIX))
    else:
        form = AddClient()
    return render(request, 'add_client.html', {'form': form})


def confirm_user(request, uuid=None):
    try:
        pending_user = PendingUsers.objects.get(key=uuid)
    except PendingUsers.DoesNotExist:
        return render(request, 'invalid_confirm_url.html')
    # give them a password
    password_chars = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    password = ''.join(random.sample(password_chars, 8))

    # create the user
    new_user = User.objects.create_user(first_name=pending_user.first_name, last_name=pending_user.last_name,
                                        username=pending_user.email, email=pending_user.email, phone_number=pending_user.phone_number, password=password)

    new_user.save()

    # email the new user
    send_email(pending_user.email, 'Your earlybird account has been activated!',
               'Welcome to earlybird, {first} {last}! <br />'
               'Your password is {password} <br />'
               '<a href="{url}">Click this link to change your password</a>'
               ''.format(first=pending_user.first_name, last=pending_user.last_name, password=password, url='http://engineering.purdue.edu/account/change_password'))

    pending_user.delete()

    return render(request, 'user_created.html', {
        'name': '{} {}'.format(pending_user.first_name, pending_user.last_name),
        'email': pending_user.email,
    })


@login_required
def settings_page(request):
    return render(request, 'acct_settings.html')
