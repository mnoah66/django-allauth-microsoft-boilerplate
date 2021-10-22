# config/views.py
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class Home(TemplateView):
    template_name = 'home.html'

@login_required
def Upload(request):
    return render(request, 'upload.html')