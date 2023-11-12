
from django.urls import path
from .views import TodoView, SpecificTodoView

urlpatterns = [
    path("todo/", TodoView.as_view()),
    path("todo/<int:id>", SpecificTodoView.as_view())
]