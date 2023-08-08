from rest_framework import serializers
from ..models import Comment
from users.api.serializer import UserSerializer
from posts.api.serializer import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    #author = UserSerializer()
    #post = PostSerializer()
    
    class Meta:
        model = Comment
        fields = ['id','content','created_at','author','post']
        