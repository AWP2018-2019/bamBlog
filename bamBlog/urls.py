"""bamBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from django.contrib import admin
from app.views import (

    HomePageView,
    CommentCreateView,
    CommentEditView,
    CommentDeleteView,
    PostCreateView,
    PostEditView,
    PostDeleteView,
    PostListView,
    PostDetailView,
)
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^post/(?P<pk>[0-9]+)/comment/create$', CommentCreateView.as_view(), name='comment_create'),
    url(r'^post/(?P<pk>[0-9]+)/comment/(?P<pk_comment>[0-9]+)/edit$', CommentEditView.as_view(), name='comment_edit'),
    url(r'^post/(?P<pk>[0-9]+)/comment/(?P<pk_comment>[0-9]+)/delete$', CommentDeleteView.as_view(), name='comment_delete'),
    url(r'^post/$', PostListView.as_view(), name = 'post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name ='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)$', PostCreateView.as_view(), name ='post_create'),
    url(r'^post/(?P<pk>[0-9]+)$', PostEditView.as_view(), name='post_update'),
    url(r'^post/(?P<pk>[0-9]+)$', PostDeleteView.as_view(), name='post_delete'),

]
