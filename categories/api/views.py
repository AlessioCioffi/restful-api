from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializer import CategorySerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # Sistema de filtro aplicado al queryset//no necesita especificarlo en el path en insomnia
    #queryset = Category.objects.filter(published=True)
    # Con el lookup cambiamos la llave única id con slug; el path pedirá slug
    #lookup_field = 'slug'
    # sistema de filtros con django-filter
    filter_backends = [DjangoFilterBackend]
    # añadir al path ej. /?published=false
    filterset_fields = ['published','title']
    