from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework import generics, permissions
from utils.permissions import IsOwnerOrReadOnly

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
