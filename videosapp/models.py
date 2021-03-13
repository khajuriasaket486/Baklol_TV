from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VideosModel(models.Model):
    tittle = models.CharField(max_length=400,default=False)
    link = models.URLField()
    is_published = models.BooleanField()
    is_trending = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tittle