import logging

from rest_framework import mixins, viewsets

from django_project.auth_.models import MyUser
from django_project.exhibition.models import Exhibition, Picture
from django_project.exhibition.serializers import ExhibitionSerializer, PictureSerializer

logger = logging.getLogger('exhibition')


class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer


class PictureViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = PictureSerializer

    def get_queryset(self):
        return Picture.objects.filter(exhibition=self.kwargs.get('parent_lookup_exhibition'))

    def perform_create(self, serializer):
        exhibition = Exhibition.objects.get(id=self.kwargs.get('parent_lookup_exhibition'))
        author = MyUser.objects.get(id=self.request.data.get('author'))
        picture = serializer.save(exhibition=exhibition, author=author)

        logger.info(f'Picture object created, ID: {picture.id}')

