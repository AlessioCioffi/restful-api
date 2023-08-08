from rest_framework.viewsets import ModelViewSet
from ..models import Comment
from .serializer import CommentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadAndCreateOnly


class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # ordenar los comentarios por fecha
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['created_at']
    filterset_fields = ['post']
    