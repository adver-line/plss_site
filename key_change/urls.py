from django.urls import path
from . import views

app_name = "key_change"

urlpatterns = [
    path("list/", views.KeyDetailView.as_view(), name="key_list"),
    path("<int:pk>", views.key_detail, name="key_encoding"),
]
