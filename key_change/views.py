from django.shortcuts import render
from slot import models
import urllib.parse
# Create your views here.


def index(request):
    slot = models.Slot.objects.all()
    return render(request, "key_change/key_list.html", {"slots": slot})


def key_detail(request, pk):
    key_word_slot = models.Slot.objects.get(pk=pk)
    key_words = key_word_slot.serch_key
    key_words = "".join(key_words)
    key_words = key_words.replace(", ", ",")
    key_words = key_words.split(',')
    re_keyword_list = []
    print(key_words)

    for key_word in key_words:
        re_keyword_list.append(key_word)
        qu_key = urllib.parse.quote(key_word)
        qu_key = f'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={qu_key}'
        re_keyword_list.append(qu_key)

    print(re_keyword_list)

    return render(request, "key_change/key_detail.html", {
        "enc_keys":re_keyword_list
    })