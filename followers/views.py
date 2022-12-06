from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Followers
from .serializers import FollowerSerializer


class FollowersList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowersDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Followers.objects.all()
