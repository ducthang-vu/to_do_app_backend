from django.contrib import admin
from django.contrib.auth.models import User
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
