from django.shortcuts import render
from django.http import HttpResponse



def handler404(request, exception):
    return render(request, '404.html', status=404)





from .models import Post  

def post_view(request):
    posts = Post.objects.all()
    return render(request, 'my_app/posts.html', {'posts': posts})


from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'my_app/post_detail.html', {'post': post})
