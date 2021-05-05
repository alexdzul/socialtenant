from django.shortcuts import render
from django.views.generic import View, ListView
from django.urls import resolve
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 100
    template_name = "index.html"
