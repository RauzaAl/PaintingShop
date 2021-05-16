from rest_framework import serializers
from django_project.utils.validators import empty_title_validator

from django_project.auth_.serializers import UsersSerializer
from django_project.exhibition.models import Exhibition, Picture


class ExhibitionSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[empty_title_validator])

    class Meta:
        model = Exhibition
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):

    exhibition = ExhibitionSerializer(read_only=True)
    author = UsersSerializer(read_only=True)

    class Meta:
        model = Picture
        fields = '__all__'
