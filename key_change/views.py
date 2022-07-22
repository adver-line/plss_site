from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from users import mixins as user_mixins
from slot import models
import urllib.parse

#
# def index(request):
#     slot = models.Slot.objects.all()
#     return render(request, "key_change/key_list.html", {"slots": slot})


class KeyDetailView(user_mixins.LoggedInOnlyView, ListView):
    model = models.Slot
    paginate_by = 10
    ordering = "id"
    context_object_name = "slots"
    template_name = "key_change/key_list.html"


    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     print(qs)
    #     user = self.request.user
    #     if not user.is_superuser:
    #         qs = qs.filter(slot_host__email=user.email)
    #     return qs





def key_detail(request, pk):
    key_word_slot = get_object_or_404(models.Slot, pk=pk)
    # key_word_slot = models.Slot.objects.get(pk=pk)
    key_words = key_word_slot.serch_key
    # key_words = "".join(key_words)
    key_words = key_words.replace(", ", ",")
    key_words = key_words.split(',')
    re_keyword_list = []

    for key_word in key_words:
        qu_key = urllib.parse.quote(key_word)

        if key_word_slot.product_choices == "단일상품":
            qu_key = f'https://msearch.shopping.naver.com/search/all?query={qu_key}'
        else:
            naver_url = key_word_slot.product_url
            qu_key = f'{naver_url}?query={qu_key}'

        key_dic = {"key":key_word, "key_url":qu_key}
        re_keyword_list.append(key_dic)



    return render(request, "key_change/key_detail.html", {
        "enc_keys":re_keyword_list,
        "slots":key_word_slot,
    })