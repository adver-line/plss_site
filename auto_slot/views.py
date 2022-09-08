from django.http import Http404
from django.urls import reverse_lazy
from users import mixins as user_mixins
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView, ListView, FormView
from . import models, forms


class AutoSlotView(user_mixins.LoggedInOnlyView, ListView):

    model = models.AutoSlot
    paginate_by = 10
    ordering = "id"
    context_object_name = "slots"
    template_name = "auto_slot/autoslot_list.html"


    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(slot_host__email=user.email)
        return qs



class AutoUpdateSlotView(
    user_mixins.LoggedInOnlyView,
    UpdateView,
):

    model = models.AutoSlot
    fields = (
        "serch_key",
    )

    template_name = "auto_slot/update_auto_slot.html"

    success_message = "슬롯이 업데이트 되었습니다."

    def get_object(self, queryset=None):
        slot = super().get_object(queryset=queryset)
        if not self.request.user.is_superuser:
            if slot.slot_host.pk != self.request.user.pk:
                raise Http404()
        return slot

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["serch_key"].label = "자동완성 키워드를 입력해주세요."
        return form

    def form_valid(self, form):
        id_s = self.object.pk
        last = models.AutoSlot.objects.get(pk=id_s)
        change_str = ""

        if last.serch_key != self.object.serch_key:
            print(f'스토어명 변경 : [{last.serch_key}] => [{self.object.serch_key}]')
            change_str = change_str + f'스토어명 변경 [{last.serch_key}] => [{self.object.serch_key}] \n'
            self.object.modyfi_check = True

        self.object.changed_memo = change_str
        self.object.save()
        return super().form_valid(form)


    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("auto_slot:auto_click")


class AuotClickCreateView(
    user_mixins.LoggedInOnlyView,
    FormView,
):

    template_name = "auto_slot/create-slot-click.html"
    form_class = forms.AutoSlotCreateForm
    success_url = reverse_lazy("auto_slot:auto_click")

    # initial = {"first_name": "pk", "last_name": "yo", "email": "la@las.com"}

    def form_valid(self, form):
        slot = form.save()
        slot.slot_host = self.request.user
        slot.save()

        return redirect(reverse("auto_slot:auto_click"))