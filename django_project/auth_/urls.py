from django.urls import path
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from django_project.auth_.views import register, UsersViewSet

router = ExtendedSimpleRouter()

router.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('register/', register),
    path('login/', obtain_jwt_token),
]

urlpatterns += router.urls
