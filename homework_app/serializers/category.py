from rest_framework import serializers

from homework_app.models.task import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'