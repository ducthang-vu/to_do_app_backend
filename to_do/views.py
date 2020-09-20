from django.contrib.auth.models import User
from rest_framework import viewsets
from to_do.serializers import UserSerializer, TaskSerializer
from rest_framework import permissions
from to_do.permissions import IsCreator


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.IsAdminUser


class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = TaskSerializer
    permission_classes = permissions.IsAdminUser, permissions.IsAuthenticated, IsCreator

    def get_queryset(self):
        return self.request.user.tasks.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
