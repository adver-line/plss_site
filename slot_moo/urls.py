from django.urls import path
from slot_moo import views

app_name = "slot_moo"

# urlpatterns = [
#     path("<int:pk>", views.slot_detail, name="detail"),
# ]


urlpatterns = [
    path("list/", views.HomeView.as_view(), name="slot_moo_list"),
    path("edit/<int:pk>/", views.UpdateSlotMooView.as_view(), name="slot_moo_detail"),
    path("click/create/", views.SlotMooClickCreateView.as_view(), name="slot_moo_create"),
]
