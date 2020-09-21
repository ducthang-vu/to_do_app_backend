from django.contrib.auth.models import User
from rest_framework import viewsets
from to_do.serializers import UserSerializer, TaskSerializer
from rest_framework import permissions
from to_do.permissions import IsCreator


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes_by_action = {
                                        'create': (permissions.AllowAny,),
                                        'list': (permissions.IsAdminUser,),
                                        'default': (permissions.IsAuthenticated,),
                                    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes_by_action['default']]

    def get_queryset(self):
        return User.objects.all() if self.action == 'list' else User.objects.filter(pk=self.request.user.id)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = permissions.IsAdminUser | permissions.IsAuthenticated, IsCreator

    def get_queryset(self):
        return self.request.user.tasks.all()
    '''
    def get_permissions(self):
        return permissions.IsAdminUser | permissions.IsAuthenticated if self.action == 'create' \
                   else permissions.IsAdminUser | permissions.IsAuthenticated, IsCreator
    '''
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
