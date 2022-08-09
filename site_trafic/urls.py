from django.urls import path
from . import views

app_name = "site_trafic"

# urlpatterns = [
#     path("<int:pk>", views.slot_detail, name="detail"),
# ]


urlpatterns = [
    path("web_click/", views.SiteSlotView.as_view(), name="web_click"),
    path("web_click/edit/<int:pk>/", views.UpdateSiteSlotView.as_view(), name="web_click_edit"),
]
