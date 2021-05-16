from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
import logging
from django_project.main.models import Artist, Client
from django_project.main.serializers import ArtistSerializer, ClientSerializer

logger = logging.getLogger('main')


class ArtistApiViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def list(self, request, *args, **kwargs):
        super().list(request, args, kwargs)

        logger.debug(f'View information about artist: ')


class ClientApiViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.prefetch_related('books')
    serializer_class = ClientSerializer
    permission_classes = (AllowAny,)


