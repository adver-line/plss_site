from django.urls import path
from slot import views

app_name = "slot"

# urlpatterns = [
#     path("<int:pk>", views.slot_detail, name="detail"),
# ]


urlpatterns = [
    path("list/", views.HomeView.as_view(), name="slot_list"),
    path("edit/<int:pk>/", views.UpdateSlotView.as_view(), name="detail"),
]
