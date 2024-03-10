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
from rest_framework import status
from rest_framework.response import Response

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def delete(self, request, *args, **kwargs):
        snippet = self.get_object()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer