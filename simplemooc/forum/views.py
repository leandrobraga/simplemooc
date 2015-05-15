from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import ListView

from .models import Thread


class ForumView(ListView):

    model = Thread
    paginate_by = 10
    template_name = "forum/index.html"

index = ForumView.as_view()
