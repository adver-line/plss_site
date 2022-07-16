from django.urls import path
from . import views

app_name = "slot"

# urlpatterns = [
#     path("<int:pk>", views.slot_detail, name="detail"),
# ]


urlpatterns = [
    path("<int:pk>", views.UpdateSlotView.as_view(), name="detail"),
]
