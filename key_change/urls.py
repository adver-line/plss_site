from django.urls import path
from . import views

app_name = "key_change"

urlpatterns = [
    path("list/", views.index, name="key_list"),
    path("<int:pk>", views.key_detail, name="key_encoding"),
]
