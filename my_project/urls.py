"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.conf.urls import handler404
from my_app.views import handler404  
handler404 = 'my_app.views.handler404'


from django.urls import path, include
from my_app.views import post_view  


from django.contrib import admin
from django.urls import path, include
from my_app.views import post_view
from my_app.views import post_detail  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', post_view, name='post_view'),
    path('post/<int:post_id>/', post_detail, name='post_detail'), 
]

from django.urls import path
from my_app.views import SnippetList, SnippetDetail

urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
]

from django.urls import path
from my_app.views import YourModelDeleteAPIView

urlpatterns = [
    path('your-models/<int:pk>/', YourModelDeleteAPIView.as_view(), name='your-model-delete'),
]
