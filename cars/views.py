from django.shortcuts import render
from . import models

def postView(request):
    post_value = models.Post.objects.all()
    context = {
        'post_key': post_value,
    }
    return render(request, 'post.html', context)