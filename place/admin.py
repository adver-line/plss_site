from django.contrib import admin
from . import models


@admin.register(models.PlaceClick)
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
            "날짜 및 타수",
            {"fields": ("day_count", "click_count")},
        ),
        (
            "키워드 및 제품",
            {
                "fields": (
                    "serch_key",
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
            {"fields": ("app_code_str",)},
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
        "click_count",
        "serch_key",
        "store_names",
        "slot_start_date",
        "slot_end_date",
        "modyfi_check",
        "update",
        "app_link",
    )
    # models.slot_host.short_description = "아이디"

    list_filter = (
        "slot_status",
        "modyfi_check",
        "slot_end_date",
        "update",
        "slot_host",
    )

    # search_fields = ("product_name",)
    search_fields = ("slot_host__username", "pk")
    raw_id_fields = ("slot_host",)
    verbose_name = "플레이스 트래픽 관리"

    # fieldsets = UserAdmin.fieldsets + (("회사명", {"fields": ("corpname",)}),)






@admin.register(models.PlaceSave)
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
            "날짜 및 타수",
            {"fields": ("day_count", "click_count")},
        ),
        (
            "키워드 및 제품",
            {
                "fields": (
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
            {"fields": ("app_code_str",)},
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
        "store_names",
        "click_count",
        "slot_start_date",
        "slot_end_date",
        "modyfi_check",
        "update",
        "app_link",
    )
    # models.slot_host.short_description = "아이디"

    list_filter = (
        "slot_status",
        "modyfi_check",
        "slot_end_date",
        "update",
        "slot_host",
    )

    # search_fields = ("product_name",)
    search_fields = ("slot_host__username", "pk")

    raw_id_fields = ("slot_host",)
    # verbose_name = "실유저 슬롯 관리"

    # fieldsets = UserAdmin.fieldsets + (("회사명", {"fields": ("corpname",)}),)

    @admin.register(models.PlaceKeep)
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
                "날짜 및 타수",
                {"fields": ("day_count", "click_count")},
            ),
            (
                "키워드 및 제품",
                {
                    "fields": (
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
                {"fields": ("app_code_str",)},
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
            "click_count",
            "slot_start_date",
            "slot_end_date",
            "modyfi_check",
            "update",
            "app_link",
        )
        # models.slot_host.short_description = "아이디"

        list_filter = (
            "slot_status",
            "modyfi_check",
            "slot_end_date",
            "update",
            "slot_host",
        )

        search_fields = ("slot_host__username", "pk")
        raw_id_fields = ("slot_host",)