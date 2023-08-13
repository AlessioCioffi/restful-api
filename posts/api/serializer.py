from rest_framework import serializers
from ..models import Post
from users.api.serializer import UserSerializer
from categories.api.serializer import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    
    class Meta:
        model = Post
        fields = ['id','title','content','slug','miniature','created_at','published','author','category']