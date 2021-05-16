from rest_framework import serializers
from django_project.main.models import Artist, Client
from django_project.exhibition.serializers import PictureSerializer


class ClientSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'address', 'pictures')


class ArtistSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name', 'email', 'pictures', 'photo')