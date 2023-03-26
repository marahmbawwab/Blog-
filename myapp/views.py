from django.shortcuts import render
from .models import posts
# Create your views here.


def index(request):
    all_posts = posts.objects.all()
    return render(request, 'index.html', {'posts': all_posts})


def post(request, pk):
    one_posts = posts.objects.get(id=pk)
    return render(request, 'post.html', {'posts': one_posts})
