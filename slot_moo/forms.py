from django import forms
from . import models
from datetime import datetime, timedelta


class SlotMooCreateForm(forms.ModelForm):


    class Meta:
        model = models.SlotMoo
        fields = ("serch_key", "product_mid", "product_url",)

        labels = {
            "serch_key": "유입 키워드 입력(순위에 없는 키워드도 가능)",
            "product_mid": "제품의 mid값을 입력해주세요. (가격비교의 경우 판매처 mid)",
            "product_url": "상품 링크 주소",
        }

    def save(self, *args, **kwargs):
        slot = super().save(commit=False)
        now = datetime.now()
        slot.slot_start_date = now + timedelta(days=1)
        slot.slot_end_date = now + timedelta(days=30)
        slot.modyfi_check = True
        slot.slot_status = "대기"

        return slot