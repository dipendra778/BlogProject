
from django.db import models
from django.utils import timezone
# Create your models here.


class PostArticles(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    slug=models.CharField(max_length=40)
    image=models.FileField(blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    description=models.CharField(max_length=3000)

    def __str__(self):
        return self.title




