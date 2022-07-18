from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
