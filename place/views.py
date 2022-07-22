from django.http import Http404
from users import mixins as user_mixins
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView, ListView
from . import models


class PlaceSlotView(user_mixins.LoggedInOnlyView, ListView):

    model = models.PlaceClick
    paginate_by = 10
    ordering = "id"
    context_object_name = "slots"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(slot_host__email=user.email)
        return qs


class UpdateSlotView(
    user_mixins.LoggedInOnlyView,
    UpdateView,
):

    model = models.PlaceClick
    fields = (
        "serch_key",
        "product_url",
        "store_names",
    )

    template_name = "place/update-slot.html"

    success_message = "슬롯이 업데이트 되었습니다."

    def get_object(self, queryset=None):
        slot = super().get_object(queryset=queryset)
        if not self.request.user.is_superuser:
            if slot.slot_host.pk != self.request.user.pk:
                raise Http404()
        return slot

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields[
            "serch_key"
        ].label = """제품 키워드 입력
( 검색 순위 15위 이내로 세팅해주세요.
// 100타 당 키워드 1개 콤마 구분 =>예) 캠핑, 캠핑의자, 캠핑체어
// 세팅 안하시면 오버플 납니다.)"""


        form.fields["product_url"].label = "상품 링크 (가격비교는 원부주소)"
        form.fields["store_names"].label = "판매처 (가격비교는 판매처 이름 작성)"
        return form