# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.forms import CommentForm
from app.models import Post, Comment


# Create your views here.


class HomePageView(TemplateView):

    template_name = "index.html"

@login_required

def comment_create(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(id=pk)
            Comment.objects.create(
                created_by = request.user,
                post = post,
                **form.cleaned_data
            )
            return redirect(reverse_lazy("post_detail", kwargs={"pk": pk}))


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs['pk'])
        Comment.objects.create(
            created_by=self.request.user,
            post=post,
            **form.cleaned_data
        )
        return redirect(reverse_lazy("post_detail", kwargs={"pk": self.kwargs['pk']}))


class CommentEditView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['text']
    pk_url_kwarg = 'pk_comment'
    template_name = 'comment_update.html'

    def form_valid(self, form):
        comment = Comment.objects.get(pk=self.kwargs['pk_comment'])
        comment.text = form.cleaned_data['text']
        comment.save()
        return redirect(reverse_lazy("post_detail", kwargs={"pk": self.kwargs['pk']}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "comment_delete.html"
    model = Comment
    pk_url_kwarg = 'pk_comment'

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs['pk']})



