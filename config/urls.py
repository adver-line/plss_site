"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("slot/", include("slot.urls", namespace="slot")),
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
]

admin.site.site_header = "실유저 슬롯 관리자"
admin.site.site_title = "실유저 슬롯 관리자"
admin.site.index_title = "유저 및 슬롯 관리 페이지"
