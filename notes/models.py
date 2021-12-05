from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    # Le propriétaire (owner)est un objet User , que nous importons depuis le module auth de Django.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title