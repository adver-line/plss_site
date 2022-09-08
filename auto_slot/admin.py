from django.contrib import admin
from . import models


@admin.register(models.AutoSlot)
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
            "자동완성 키워드",
            {
                "fields": (
                    "serch_key",
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
        "slot_start_date",
        "slot_end_date",
        "modyfi_check",
        "update",
    )
    # models.slot_host.short_description = "아이디"

    list_filter = (
        "slot_status",
        "serch_key",
        "modyfi_check",
        "slot_end_date",
        "update",
        "slot_host",
    )

    # search_fields = ("product_name",)
    search_fields = ("slot_host__username", "pk")
    raw_id_fields = ("slot_host",)
    verbose_name = "자동완성 슬롯 관리"

    # fieldsets = UserAdmin.fieldsets + (("회사명", {"fields": ("corpname",)}),)




