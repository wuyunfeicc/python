from django.db import models
from django.utils import timezone
# Create your models here.
class BlogArticle(models.Model):
    title=models.CharField(max_length=100)
    autor= models.CharField(max_length=50)
    content = models.TextField()
    add_time=models.DateTimeField(default=timezone.now)
