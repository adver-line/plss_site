from django.urls import URLPattern, path
from slot import views as slot_views

app_name = "core"

urlpatterns = [path("", slot_views.HomeView.as_view(), name="home")]
