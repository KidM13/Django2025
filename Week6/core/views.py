from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
from .models import Post

def home(request):
    return HttpResponse("Hello Blog")

class WelcomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django CBV")
    


def post_titles(request):
    posts = Post.objects.all()
    titles = [post.title for post in posts]
    return HttpResponse("<br>".join(titles))

