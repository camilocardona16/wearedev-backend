# views.py
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.GenericViewSet, 
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Asegura que solo los usuarios autenticados puedan acceder
    
    def perform_create(self, serializer):
        # Asocia la tarea con el usuario autenticado
        serializer.save(user=self.request.user)