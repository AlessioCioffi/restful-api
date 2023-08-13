from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializer import CategorySerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    # añadir al path ej. /?published=false
    filterset_fields = ['published','title']
    