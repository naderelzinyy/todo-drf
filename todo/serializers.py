"""To-do serializer file."""
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    # def update(self, instance, validated_data):
    #     print(f"{validated_data = }")
    #     instance.save()
    #     return instance

    class Meta:
        model = Todo
        fields = "__all__"
