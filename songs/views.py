from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Song
from .serializers import SongSerializer


class CustomPagination(PageNumberPagination):
    page_size = 1


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get('pk'))
