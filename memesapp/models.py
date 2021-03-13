from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MemesModel(models.Model):
    tittle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='memes/')
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tittle
