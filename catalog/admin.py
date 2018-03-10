from django.contrib import admin

# Register your models here.

from .models import ModelPerson, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class ModelPersonAdmin(admin.ModelAdmin):
    fields = ('email', 'first_name', 'last_name', 'nickname',)
    list_display = ('id', 'email', 'first_name', 'last_name', 'nickname',)
    inlines = [PhotoInline]


class PhotoAdmin(admin.ModelAdmin):
    fields = ('location', 'model_person',)
    list_display = ('location', 'model_person',)


admin.site.register(ModelPerson, ModelPersonAdmin)
admin.site.register(Photo, PhotoAdmin)
