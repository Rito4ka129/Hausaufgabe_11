from rest_framework import serializers
from homework_app.models.task import Task, SubTask, Category
from datetime import date


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        read_only_fields = ('created_at',)


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SubTaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']

    def validate_deadline(self, value):
        if value < date.today():
            raise serializers.ValidationError("Дата не может быть в прошлом.")
        return value
