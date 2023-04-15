from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.models import User
from django.template import loader

def index(request):
    user_lists = User.objects.all()
    template = loader.get_template("Blog/index.html")
    context = {
        "users": user_lists,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
