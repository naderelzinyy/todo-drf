from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer

TODO_FIELDS = [field.name for field in Todo._meta.get_fields()]


class TodoView(APIView):
    """To-do view."""
    http_method_names = ['get', 'post']

    @staticmethod
    def get(request):
        """Get logic of TodoView."""

        return Response({
            "result": list(Todo.objects.values("title", "description", "is_completed"))
        })

    @staticmethod
    def post(request):
        """POST logic of TodoView."""
        serializer = TodoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'result': serializer.errors})

        serializer.save()
        return Response({
            "result": "Todo added successfully!"
        })


class SpecificTodoView(APIView):
    http_method_names = ['delete', 'patch']

    def patch(self, request, id):
        """PATCH logic of TodoView."""
        if all(element not in request.data for element in TODO_FIELDS):
            return Response({"result": "No such a key"})

        if todo := Todo.objects.filter(id=id).first():
            ser = TodoSerializer(instance=todo, data=request.data, partial=True)
            if ser.is_valid(raise_exception=True):
                ser.update(instance=todo, validated_data=request.data)
                return Response({"result": "Updated todo successfully"})
        return Response({"result": "no todo found"})

    def delete(self, request, id):
        """DELETE logic of To-do."""
        try:
            if todo := Todo.objects.filter(id=id):
                todo.delete()
                return Response({"result": f"Deleted {id}. Todo successfully!"})

            return Response({"result": f"No {id}. Todo found!"})

        except Exception:
            return Response({"result": f"Couldn't delete {id}. Todo"})
