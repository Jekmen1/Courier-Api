from rest_framework import permissions
from rest_framework.response import Response
class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.role == request.user or request.user.is_staff

class IsCourierOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.courier == request.user or request.user.is_staff

class CustomerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.role == request.user
class ParcelPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user.is_authenticated and request.user.role == 'customer':
            return True

        return False
class CourierPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ['PUT', 'PATCH']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        try:
            return obj.courier == request.user
        except AttributeError:
            return Response('You have not Permissions')

class AdminPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff
