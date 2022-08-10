from django import forms
from . import models
from django.utils import timezone
from datetime import datetime, timedelta


class PlaceSlotCreateForm(forms.ModelForm):


    class Meta:
        model = models.PlaceClick
        fields = ("day_count", "click_count", "serch_key", "store_names", "product_url",)

        labels = {
            "day_count": "슬롯 기간 선택",
            "click_count": "하루 클릭수(1일 기준 타수를 입력해주세요)",
            "serch_key": "방문 유입 키워드(검색 시 30위 이내 키워드로 세팅해 주세요)",
            "store_names": "네이버 플레이스 URL(꼭 모바일 주소를 기입해 주세요. 예 - https://m.place.naver.com/1111111)",
            "product_url": "가게상호",
        }

    def save(self, *args, **kwargs):
        slot = super().save(commit=False)
        now = datetime.now()
        slot.slot_start_date = now + timedelta(days=1)

        day = slot.day_count

        if day == "3일":
            slot.slot_end_date = now + timedelta(days=3)
        elif day == "7일":
            slot.slot_end_date = now + timedelta(days=7)
        elif day == "10일":
            slot.slot_end_date = now + timedelta(days=10)
        elif day == "20일":
            slot.slot_end_date = now + timedelta(days=20)
        elif day == "30일":
            slot.slot_end_date = now + timedelta(days=30)

        slot.modyfi_check = True

        return slot