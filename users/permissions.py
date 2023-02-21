from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return request.user.id == obj.id or request.user.is_superuser
