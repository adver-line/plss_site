from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from core import models as core_models
from users import models as users_models
from django.shortcuts import reverse


class AutoSlot(core_models.TimeStampedModel):

    """자동완성 슬롯 모델"""
    SLOT_STATUS = "대기"
    SLOT_STATUS1 = "진행"
    SLOT_STATUS2 = "중지"
    SLOT_STATUS3 = "종료"

    SLOT_CHOICES = (
        (SLOT_STATUS, "대기"),
        (SLOT_STATUS1, "진행"),
        (SLOT_STATUS2, "중지"),
        (SLOT_STATUS3, "종료"),
    )

    day_count = models.CharField(default="25일", max_length=3, blank=True)
    serch_key = models.CharField(max_length=100, default="", blank=True, null=True)
    modyfi_check = models.BooleanField(default=False)
    slot_start_date = models.DateField(blank=True, null=True)
    slot_end_date = models.DateField(blank=True, null=True)
    slot_host = models.ForeignKey(
        users_models.User, related_name="auto_slot_model", on_delete=models.CASCADE
    )
    # app_code_str = models.CharField(max_length=100, blank=True, null=True)
    slot_status = models.CharField(choices=SLOT_CHOICES, default="SLOT_STATUS", blank=True, null=True, max_length=6)
    changed_memo = models.TextField(blank=True, null=True)

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
        verbose_name_plural = "자동완성 슬롯 관리"
        ordering = ["id"]
        # verbose_name_pu

    def get_absolute_url(self):
        return reverse("core:home")

    def return_id_corp(self):
        host = self.slot_host
        corp = host.corpname
        re_text = f'{host} \n {corp}'
        return re_text

    return_id_corp.short_description = "아이디//회사명"