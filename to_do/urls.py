from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from to_do import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='User')
router.register(r'tasks', views.TaskViewSet, basename='Task')

urlpatterns = [
    re_path(r'^', include(router.urls))
]
