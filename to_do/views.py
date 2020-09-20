from django.http import Http404
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from to_do.models import Task
from to_do.serializers import UserSerializer, TaskSerializer
from rest_framework import permissions
from to_do.permissions import IsCreator


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''
class TaskIndex(APIView):
    """
    List all tasks, or create a new task.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskElement(APIView):
    """
    Retrieve, update or delete a task instance.
    """
    permission_classes = [permissions.IsAuthenticated, IsCreator]

    def get_task(self, task_id):
        try:
            return Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, task_id, format=None):
        task = self.get_task(task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, task_id, format=None):
        task = self.get_task(task_id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, format=None):
        task = self.get_task(task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly, IsCreator

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
