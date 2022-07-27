# Generated by Django 4.1rc1 on 2022-07-27 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slot", "0007_slot_app_code_slot_order_num"),
    ]

    operations = [
        migrations.AddField(
            model_name="slot",
            name="slot_status",
            field=models.CharField(
                blank=True,
                choices=[("대기", "대기"), ("진행", "진행"), ("중지", "중지"), ("종료", "종료")],
                default="SLOT_STATUS",
                max_length=6,
                null=True,
            ),
        ),
    ]
