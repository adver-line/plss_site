from urllib import request
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

from core import models as core_models
from users import models as users_models
from django.shortcuts import reverse
import urllib.parse


# Create your models here.
class Slot(core_models.TimeStampedModel):

    """Slot Models"""

    DAY3 = "3일"
    DAY7 = "7일"
    DAY10 = "10일"
    DAY20 = "20일"
    DAY30 = "30일"

    DAY_CHOICES = (
        (DAY3, "3일"),
        (DAY7, "7일"),
        (DAY10, "10일"),
        (DAY20, "20일"),
        (DAY30, "30일"),
    )

    PRODUCT_NUM1 = "단일상품"
    PRODUCT_NUM2 = "가격비교상품"

    PRODUCT_CHOICES = (
        (PRODUCT_NUM1, "단일상품"),
        (PRODUCT_NUM2, "가격비교상품"),
    )

    day_count = models.CharField(choices=DAY_CHOICES, max_length=3, blank=False)
    click_count = models.IntegerField(blank=False)
    serch_key = models.CharField(max_length=100, default="", blank=True, null=True)
    product_choices = models.CharField(
        choices=PRODUCT_CHOICES, max_length=6, blank=True, null=True
    )
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_url = models.CharField(max_length=200, blank=True, null=True)
    store_names = models.CharField(max_length=100, blank=True, null=True)
    modyfi_check = models.BooleanField(default=True)
    slot_start_date = models.DateField()
    slot_end_date = models.DateField()
    slot_host = models.ForeignKey(
        users_models.User, related_name="slots", on_delete=models.CASCADE
    )
    order_num = models.IntegerField(blank=True, null=True)
    app_code = models.IntegerField(blank=True, null=True)
    # def save(self, *args, **kwargs):
    #     print(request.user)
    #     self.modyfi_check = True
    #     super().save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return str(self.id)

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.slot_start_date and now <= self.slot_end_date

    in_progress.short_description = "슬롯 활성 상태"
    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.slot_end_date

    is_finished.short_description = "슬롯 종료 여부"
    is_finished.boolean = True

    def app_link(self):
        pk = self.pk
        return mark_safe(f"<a href='/key_change/{pk}'>바로가기</a>")


    class Meta:
        verbose_name_plural = "실유저 슬롯 관리"
        ordering = ["id"]
        # verbose_name_pu

    def get_absolute_url(self):
        return reverse("core:home")
