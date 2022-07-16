from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.db import models


# Create your models here.
class User(AbstractUser):
    corpname = models.CharField(max_length=30, default="", null=True)

    class Meta:
        verbose_name_plural = "아이디 관리"

    # def get_absolute_url(self):
    #     return reverse("users.profile", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
