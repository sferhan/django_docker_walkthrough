
from django.http import HttpResponse
from django.conf import settings


def index(req):
    return HttpResponse(f"<h1>Hello from {settings.SERVER_NAME}</h1>")