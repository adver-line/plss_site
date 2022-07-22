from tabnanny import verbose
from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Slot)
class CustomSlotAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "슬롯 등록 아이디",
            {"fields": ("slot_host",)},
        ),
        (
            "날짜 및 타수",
            {"fields": ("day_count", "click_count")},
        ),
        (
            "키워드 및 제품",
            {
                "fields": (
                    "serch_key",
                    "product_choices",
                    "product_name",
                    "product_url",
                    "store_names",
                )
            },
        ),
        (
            "수정 확인",
            {"fields": ("modyfi_check",)},
        ),
        (
            "기간",
            {"fields": ("slot_start_date", "slot_end_date")},
        ),
        (
            "APP연동",
            {"fields": ("order_num", "app_code")},
        ),
    )

    list_display = (
        "id",
        "slot_host",
        "click_count",
        "serch_key",
        # "product_choices",
        "product_name",
        # "modyfi_check",
        "slot_start_date",
        "slot_end_date",
        "in_progress",
        "is_finished",
        "update",
        "app_link",
    )
    # models.slot_host.short_description = "아이디"

    list_filter = (
        "modyfi_check",
        "slot_end_date",
        "update",
        "slot_host",
        # "in_progress",
    )

    # search_fields = ("product_name",)
    search_fields = ("slot_host__username",)

    raw_id_fields = ("slot_host",)
    # verbose_name = "실유저 슬롯 관리"

    # fieldsets = UserAdmin.fieldsets + (("회사명", {"fields": ("corpname",)}),)
