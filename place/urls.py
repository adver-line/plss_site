from django.urls import path
from . import views

app_name = "place"

# urlpatterns = [
#     path("<int:pk>", views.slot_detail, name="detail"),
# ]


urlpatterns = [
    path("click/", views.PlaceSlotView.as_view(), name="click"),
    path("click/edit/<int:pk>/", views.UpdateSlotView.as_view(), name="click_edit"),
    path("save/", views.PlaceSlotSaveView.as_view(), name="save"),
    path("save/edit/<int:pk>/", views.UpdateSlotSaveView.as_view(), name="save_edit"),
    path("keep/", views.PlaceSlotKeepView.as_view(), name="keep"),
    path("keep/edit/<int:pk>/", views.UpdateSlotKeepView.as_view(), name="keep_edit"),
]
