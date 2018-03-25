from django.urls import path

from .views import home, profile


urlpatterns = [
    path('', home),
    path('model/<nickname>', profile, name='model-profile'),
]
