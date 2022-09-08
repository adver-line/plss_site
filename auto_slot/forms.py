from django import forms
from . import models
from datetime import datetime, timedelta


class AutoSlotCreateForm(forms.ModelForm):


    class Meta:
        model = models.AutoSlot
        fields = ("serch_key",)

        labels = {
            "serch_key": "자동완성 키워드를 입력해주세요.",
        }

    def save(self, *args, **kwargs):
        slot = super().save(commit=False)
        slot.modyfi_check = True
        slot.slot_status = "대기"

        return slot