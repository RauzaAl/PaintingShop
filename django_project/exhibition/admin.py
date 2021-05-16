from django.contrib import admin

from django_project.exhibition.models import Exhibition, Picture


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'start', 'end',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'author', 'genre', 'height', 'width', 'created_at', 'exhibition')
