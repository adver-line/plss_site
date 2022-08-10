# Generated by Django 4.1rc1 on 2022-08-09 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteClick",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
                (
                    "day_count",
                    models.CharField(
                        choices=[
                            ("3일", "3일"),
                            ("7일", "7일"),
                            ("10일", "10일"),
                            ("20일", "20일"),
                            ("30일", "30일"),
                        ],
                        max_length=3,
                    ),
                ),
                ("click_count", models.IntegerField()),
                (
                    "serch_key",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "store_names",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "product_url",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("modyfi_check", models.BooleanField(default=False)),
                ("slot_start_date", models.DateField()),
                ("slot_end_date", models.DateField()),
                (
                    "slot_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("대기", "대기"),
                            ("진행", "진행"),
                            ("중지", "중지"),
                            ("종료", "종료"),
                        ],
                        default="SLOT_STATUS",
                        max_length=6,
                        null=True,
                    ),
                ),
                ("changed_memo", models.TextField(blank=True, null=True)),
                (
                    "slot_host",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="site_click_slot",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "사이트 트래픽 슬롯 관리",
                "ordering": ["id"],
            },
        ),
    ]