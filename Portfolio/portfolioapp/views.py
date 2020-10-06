from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()  # it grabs all database objects and turns them into python obj
    return render(request, 'portfolioapp/home.html', {'projects': projects})
