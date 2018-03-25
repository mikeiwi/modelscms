from django.shortcuts import render

from .models import ModelPerson


def home(request):
    models = ModelPerson.objects.all()
    return render(request, 'catalog/home.html', {'models': models})
