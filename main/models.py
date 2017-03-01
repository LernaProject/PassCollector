from django.contrib import auth
from django.db      import models


class User(models.Model):
    django_user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    user_id     = models.IntegerField(unique=True)
    username    = models.CharField(max_length=255, blank=True)
