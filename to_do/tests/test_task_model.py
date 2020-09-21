from django.test import TestCase
from to_do.models import Task
from django.contrib.auth.models import User


class TaskTestCase(TestCase):
    def setUp(self):
        user = User(username='test_user', email='test@mail.com', password='prova')
        user.save()
        Task.objects.create(title="dummy_title", description="dummy", user=user)

    def test_task_str(self):
        task = Task.objects.get(title="dummy_title")
        self.assertEqual(str(task), 'dummy_title')

    def test_task_priority_default(self):
        task = Task.objects.get(title="dummy_title")
        self.assertEqual(task.priority, 1)

    def test_task_completed_default(self):
        task = Task.objects.get(title="dummy_title")
        self.assertEqual(task.completed, False)
