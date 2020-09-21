from rest_framework import permissions


class IsCreator(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object.
    """
    message = 'You must be the creator of this task.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
