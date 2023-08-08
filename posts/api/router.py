from rest_framework.routers import DefaultRouter
from .views import PostApiViewSet

post_routers = DefaultRouter()
post_routers.register(prefix='posts',basename='posts',viewset=PostApiViewSet)