from django.http import Http404
from users import mixins as user_mixins
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView, ListView
from . import models


class HomeView(user_mixins.LoggedInOnlyView, ListView):

    model = models.Slot
    # paginate_by = 10
    ordering = "id"
    context_object_name = "slots"


def slot_detail(request, pk):
    return render(request, "slot/slot_detail.html")


class UpdateSlotView(
    user_mixins.LoggedInOnlyView,
    UpdateView,
):

    model = models.Slot
    fields = (
        "serch_key",
        "product_choices",
        "product_name",
        "product_url",
        "store_names",
    )

    template_name = "slot/update-slot.html"

    success_message = "슬롯이 업데이트 되었습니다."

    def get_object(self, queryset=None):
        slot = super().get_object(queryset=queryset)
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
        form.fields["product_choices"].label = "단일 / 가격비교 상품 선택"
        form.fields["product_name"].label = "상품명(단일) or 원부명(가격비교)"
        form.fields["product_url"].label = "상품 링크 (가격비교는 원부주소)"
        form.fields["store_names"].label = "판매처 (가격비교는 판매처 이름 작성)"
        return form
