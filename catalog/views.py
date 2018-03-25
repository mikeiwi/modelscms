from django.shortcuts import render, get_object_or_404

from .models import ModelPerson, Photo


def home(request):
    models = ModelPerson.objects.all()
    return render(request, 'catalog/home.html', {'models': models})


def profile(request, nickname):
    model = get_object_or_404(ModelPerson, nickname=nickname)
    photos = Photo.objects.filter(model_person=model)
    return render(request, 'catalog/profile.html',
                  {'model': model, 'photos': photos})
