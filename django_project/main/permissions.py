from rest_framework.permissions import IsAuthenticated
from django_project.utils.constants import USER_ROLE_ARTIST, USER_ROLE_CLIENT


class ClientPermission(IsAuthenticated):
    message = 'Вы не покупатель'

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_CLIENT


class AuthorPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_ARTIST


class SomePermission(IsAuthenticated):
    def has_permission(self, request, view, obj):
        return obj.is_active