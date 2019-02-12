from django.http import HttpResponse
from django.views.generic.base import View


class LoginPageView(View):
    def dispatch(request, *args, **kwargs):
        response_text = '<html><head></head><body>Welcome to earlybird! This is a placeholder.</body></html>'
        return HttpResponse(response_text)
