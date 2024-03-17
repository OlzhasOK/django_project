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
from .models import Snippet
from rest_framework import generics



class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet.Serializer

    def delete(self, request, *args, **kwargs):
        snippet = self.get_object()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet.Serializer


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def my_protected_view(request):
    return HttpResponse("Этот контент доступен только авторизованным пользователям.")


from rest_framework import serializers

class MyDataSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def validate_username(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Имя пользователя должно содержать не менее 3 символов.")
        return value

    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email должен быть на домене example.com.")
        return value
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyAPIView(APIView):
    def post(self, request, format=None):
        serializer = MyDataSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
