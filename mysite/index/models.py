from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
class Sorry(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name