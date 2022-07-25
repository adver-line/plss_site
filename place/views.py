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

    template_name = "place/update-slot-click.html"

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
        ].label = """방문 유입 키워드(검색 시 15위 이내 키워드로 세팅해 주세요)"""


        form.fields["product_url"].label = "네이버 플레이스 URL(꼭 모바일 주소를 기입해 주세요. 예 - https://m.place.naver.com/1111111)"
        form.fields["store_names"].label = "가게상호(띄어쓰기 까지 정확하게 입력해 주세요)"
        return form


class PlaceSlotSaveView(user_mixins.LoggedInOnlyView, ListView):

    model = models.PlaceSave
    paginate_by = 10
    ordering = "id"
    context_object_name = "slots"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(slot_host__email=user.email)
        return qs


class UpdateSlotSaveView(
    user_mixins.LoggedInOnlyView,
    UpdateView,
):

    model = models.PlaceSave
    fields = (
        "serch_key",
        "product_url",
        "store_names",
    )

    template_name = "place/update-slot-save.html"

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
        ].label = """방문 유입 키워드(검색 시 15위 이내 키워드로 세팅해 주세요)"""

        form.fields["product_url"].label = "네이버 플레이스 URL(꼭 모바일 주소를 기입해 주세요. 예 - https://m.place.naver.com/1111111)"
        form.fields["store_names"].label = "가게상호(띄어쓰기 까지 정확하게 입력해 주세요)"
        return form


class PlaceSlotKeepView(user_mixins.LoggedInOnlyView, ListView):

    model = models.PlaceKeep
    paginate_by = 10
    ordering = "id"
    context_object_name = "slots"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(slot_host__email=user.email)
        return qs



class UpdateSlotKeepView(
    user_mixins.LoggedInOnlyView,
    UpdateView,
):

    model = models.PlaceKeep
    fields = (
        "serch_key",
        "product_url",
        "store_names",
    )

    template_name = "place/update-slot-keep.html"

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
        ].label = """방문 유입 키워드(검색 시 15위 이내 키워드로 세팅해 주세요)"""

        form.fields["product_url"].label = "네이버 플레이스 URL(꼭 모바일 주소를 기입해 주세요. 예 - https://m.place.naver.com/1111111)"
        form.fields["store_names"].label = "가게상호(띄어쓰기 까지 정확하게 입력해 주세요)"
        return form