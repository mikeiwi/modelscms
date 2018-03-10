from django.db import models
from s3direct.fields import S3DirectField


class ModelPerson(models.Model):
    """Represents a person in the catalog."""
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        ordering = ('-pk',)


class Photo(models.Model):
    """An element o a Model's gallery."""
    location = S3DirectField(dest='s3_upload')
    model_person = models.ForeignKey('catalog.ModelPerson',
                                     on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ('-pk',)

    def __str__(self):
        return f"Foto {self.pk}"
