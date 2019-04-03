"""earlybird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView

from earlybird.views import acct_page, register_page, confirm_user, client_page, get_status, logout_view

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login_page.html',
                                     redirect_authenticated_user=True,
                                     extra_context={'prefix': settings.PREFIX})),
    path('account/', acct_page),
    path('register/', register_page),
    path('client_status/<client_name>', get_status),
    path('account/create_client', client_page),
    path('confirm/<uuid>/', confirm_user),
    path('account/logout', logout_view)
] + static('/static/', document_root=os.path.join(settings.BASE_DIR, 'earlybird', 'static'))
