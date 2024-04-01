from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.role == request.user or request.user.is_staff:
            return True
        else:
            return Response({'message': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

class IsCourierOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.courier == request.user or request.user.is_staff:
            return True
        else:
            return Response({'message': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

class CustomerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True
        else:
            return Response({'message': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

    def has_object_permission(self, request, view, obj):
        if obj.role == request.user:
            return True
        else:
            return Response({'message': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

class CourierPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.method in ['PUT', 'PATCH']:
            return True
        else:
            return Response({'message': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

    def has_object_permission(self, request, view, obj):
        try:
            if obj.courier == request.user:
                return True
            else:
                return Response({'message': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        except AttributeError:
            return Response({'message': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

class AdminPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return Response({'message': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
