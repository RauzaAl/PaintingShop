import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets, mixins

from django_project.auth_.models import MyUser
from django_project.auth_.serializers import RegisterSerializer, UsersSerializer


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UsersViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = MyUser.objects.all()
    serializer_class = UsersSerializer
