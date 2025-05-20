from rest_framework import generics, status
from .serializers import JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from .models import JobApplication

class JobApplicationCreateView(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    queryset = JobApplication.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)