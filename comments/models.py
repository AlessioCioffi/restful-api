from django.db import models
from users.models import User
from posts.models import Post
from django.db.models import CASCADE




# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)