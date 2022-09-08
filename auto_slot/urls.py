from django.urls import path
from . import views

app_name = "auto_slot"

# urlpatterns = [
#     path("<int:pk>", views.slot_detail, name="detail"),
# ]


urlpatterns = [
    path("slot/", views.AutoSlotView.as_view(), name="auto_click"),
    path("slot/edit/<int:pk>/", views.AutoUpdateSlotView.as_view(), name="auto_click_edit"),
    path("slot/create/", views.AuotClickCreateView.as_view(), name="auto_click_create"),
]

