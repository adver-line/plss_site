from django.http import Http404
from users import mixins as user_mixins
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView, ListView, FormView
from . import models, forms
from django.urls import reverse_lazy


class HomeView(user_mixins.LoggedInOnlyView, ListView):

    model = models.SlotMoo
    paginate_by = 10
    ordering = "id"
    context_object_name = "slots"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(slot_host__email=user.email)
        return qs


def slot_detail(request, pk):
    return render(request, "slot_moo/slot_detail.html")




class UpdateSlotMooView(
    user_mixins.LoggedInOnlyView,
    UpdateView,
):

    model = models.SlotMoo
    fields = (
        "serch_key",
        "product_mid",
        "product_url",
    )

    template_name = "slot_moo/update-slot.html"

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
        ].label = "유입 키워드 입력(순위에 없는 키워드도 가능)"
        # form.fields["product_choices"].label = "단일 / 가격비교 상품 선택"
        form.fields["product_mid"].label = "제품의 mid값을 입력해주세요. (가격비교의 경우 판매처 mid)"
        form.fields["product_url"].label = "상품 링크 주소"
        # form.fields["store_names"].label = "판매처 (가격비교는 판매처 이름 작성)"
        return form

    def form_valid(self, form):
        id_s = self.object.pk
        last = models.SlotMoo.objects.get(pk=id_s)
        change_str = ""

        if last.serch_key != self.object.serch_key:
            change_str = change_str + f'키워드 변경 [{last.serch_key}] => [{self.object.serch_key}] \n'
            self.object.modyfi_check = True

        # if last.product_choices != self.object.product_choices:
        #     change_str = change_str + f'상품선택 변경 [{last.product_choices}] => [{self.object.product_choices}] \n'
        #     self.object.modyfi_check = True

        if last.product_mid != self.object.product_mid:
            change_str = change_str + f'상품mid 변경 [{last.product_mid}] => [{self.object.product_mid}] \n'
            self.object.modyfi_check = True

        if last.product_url != self.object.product_url:
            change_str = change_str + f'상품 url 변경 [{last.product_url}] => [{self.object.product_url}] \n'
            self.object.modyfi_check = True

        # if last.store_names != self.object.store_names:
        #     change_str = change_str + f'스토어명 변경 [{last.store_names}] => [{self.object.store_names}] \n'
        #     self.object.modyfi_check = True

        self.object.changed_memo = change_str
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("slot_moo:slot_moo_list")


class SlotMooClickCreateView(
    user_mixins.LoggedInOnlyView,
    FormView,
):

    template_name = "slot_moo/create-slot-click.html"
    form_class = forms.SlotMooCreateForm
    success_url = reverse_lazy("place:click")

    # initial = {"first_name": "pk", "last_name": "yo", "email": "la@las.com"}

    def form_valid(self, form):
        slot = form.save()
        slot.slot_host = self.request.user
        slot.save()

        return redirect(reverse("slot_moo:slot_moo_list"))