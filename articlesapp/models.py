from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArticlesModel(models.Model):
    tittle = models.CharField(max_length=400)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="article_images/")
    is_trending = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tittle

class CarouselModel(models.Model):
    tittle = models.CharField(max_length=400)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="article_images/")
    is_published = models.BooleanField(default=False)
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tittle