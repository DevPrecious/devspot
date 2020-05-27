from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, profile

def index(request):
    details = Post.objects.all().order_by('-pub_date')
    about = profile.objects.all()
    return render(request, 'devspot/index.html', {'posts': details, 'prof':about})

def details(request, post_id):
    alln = Post.objects.filter(id = post_id)
    return render(request, 'devspot/post.html', {'posts': alln})



