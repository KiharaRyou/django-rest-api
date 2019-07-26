from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created', 'is_active', 'owner']

