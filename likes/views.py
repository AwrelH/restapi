from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Likes
from .serializers import LikesSerializer


class LikesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LikesSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Likes.objects.all()
