from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # configurando el acceso con mail no se puede crear un nuevo superuser
    # para hacerlo hace falta dejar email en comentario o cancelarlo