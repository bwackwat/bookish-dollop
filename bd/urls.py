"""bd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

from bd.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', user.signup, name='signup'),
    path('blogs/', blog.BlogListView.as_view(), name='blogs'),
    path('blog/create/', blog.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/', blog.BlogDetailView.as_view(), name='blog-view'),
    path('blog/update/<int:pk>/', blog.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/delete/<int:pk>/', blog.BlogDeleteView.as_view(), name='blog-delete'),
]
