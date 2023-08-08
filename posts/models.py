from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    #Si el autor se borra se quedará el post pero sin author
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    
    def __str__(self):
        # Para que en el panel ma salga el titulo del post
        return self.title