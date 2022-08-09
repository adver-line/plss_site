from django.http import Http404
from users import mixins as user_mixins
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView, ListView
from . import models


class SiteSlotView(user_mixins.LoggedInOnlyView, ListView):

    model = models.SiteClick
    paginate_by = 10
    ordering = "id"
    context_object_name = "slots"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(slot_host__email=user.email)
        return qs


class UpdateSiteSlotView(
    user_mixins.LoggedInOnlyView,
    UpdateView,
):

    model = models.SiteClick
    fields = (
        "serch_key",
        "product_url",
        "store_names",
    )

    template_name = "site_trafic/update-slot-click.html"

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
        ].label = """검색 유입 키워드"""

        form.fields["product_url"].label = "웹사이트 제목 텍스트(띄어 쓰기 까지 정확 하게 입력해 주세요.)"
        form.fields["store_names"].label = "웹사이트 URL 주소"
        return form

    def form_valid(self, form):
        id_s = self.object.pk
        last = models.SiteClick.objects.get(pk=id_s)
        change_str = ""

        if last.serch_key != self.object.serch_key:
            change_str = change_str + f'키워드 변경 [{last.serch_key}] => [{self.object.serch_key}] \n'
            self.object.modyfi_check = True

        if last.product_url != self.object.product_url:
            change_str = change_str + f'상품 url 변경 [{last.product_url}] => [{self.object.product_url}] \n'
            self.object.modyfi_check = True

        if last.store_names != self.object.store_names:
            change_str = change_str + f'스토어명 변경 [{last.store_names}] => [{self.object.store_names}] \n'
            self.object.modyfi_check = True

        self.object.changed_memo = change_str
        self.object.save()
        return super().form_valid(form)


    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("site:web_click")