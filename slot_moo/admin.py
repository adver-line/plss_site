from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.SlotMoo)
class CustomSlotAdmin(admin.ModelAdmin):



    fieldsets = (
        (
            "슬롯 등록 아이디",
            {"fields": ("slot_host",)},
        ),
        (
            "슬롯 상태",
            {"fields": ("slot_status",)},
        ),
        (
            "키워드 및 제품",
            {
                "fields": (
                    "serch_key",
                    "product_mid",
                    "product_url",
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
            "변경 메모",
            {"fields": ("changed_memo",)},
        ),
    )


    list_display = (
        "id",
        "return_id_corp",
        "slot_status",
        "serch_key",
        # "product_choices",
        "product_mid",
        "modyfi_check",
        "slot_start_date",
        "slot_end_date",
        # "in_progress",
        # "is_finished",
        "update",

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
    search_fields = ("slot_host__username", "product_mid",)

    raw_id_fields = ("slot_host",)
    # verbose_name = "실유저 슬롯 관리"

    # fieldsets = UserAdmin.fieldsets + (("회사명", {"fields": ("corpname",)}),)
