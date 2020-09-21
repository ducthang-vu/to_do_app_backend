from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User
from to_do.models import Task


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(read_only=True)
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all(), allow_null=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'email', 'tasks', 'password')

    def create(self, validate_data):
        user = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['username'],
            password=validate_data['password']
        )
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = '__all__'
