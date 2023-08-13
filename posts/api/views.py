from rest_framework.viewsets import ModelViewSet
from .serializer import PostSerializer
from .. models import Post
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    # podemos filtrar por categoría mediante id o title
    filterset_fields = ['category','category__title']
    #http://127.0.0.1:8000/api/posts/?category__title=Barcos
    #http://127.0.0.1:8000/api/posts/?category=8
    
