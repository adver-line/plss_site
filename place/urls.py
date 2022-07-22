from django.urls import path
from . import views

app_name = "place"

# urlpatterns = [
#     path("<int:pk>", views.slot_detail, name="detail"),
# ]


urlpatterns = [
    path("click/", views.PlaceSlotView.as_view(), name="click"),
    path("edit/<int:pk>/", views.UpdateSlotView.as_view(), name="detail"),

]
