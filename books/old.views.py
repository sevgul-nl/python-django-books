from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import Book


def index(request):
    # name = request.GET.get("name") or "."
    # return HttpResponse("{} was here !..".format(name))
    return render(request, "../dj_books/templates/base.html")


def home(request):
    message = "<html><h1>Welcome to my Website</h1></html>"
    return HttpResponse(message)


class Homec(TemplateView):
    template_name = "home.html"


def welcome_view1(request):
    message = f"<html><h1>Welcome to Books!</h1> <p>{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(message)


def welcome_view(request):
    message = f"<html><h1>Welcome to Books!..</h1> \
              <p>{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(message)
