from django.db import models
from datetime import datetime

# Create your models here.
class Blog (models.Model):
   # Default behaviour - Django creates primary keys for you
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
