from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from homework_app.models.task import Category
from homework_app.serializers.category import CategorySerializer

class CategoryViewSet(ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    @action(detail=True, methods=['get'], url_path='count-tasks')
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = category.tasks.count()  # assuming you have a related_name='tasks' in the Task model
        return Response({'category_id': pk, 'task_count': task_count})
