# Generated by Django 4.1rc1 on 2022-07-27 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("place", "0002_placesave_placekeep"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="placekeep",
            options={"ordering": ["id"], "verbose_name_plural": "플레이스 KEEP 슬롯 관리"},
        ),
        migrations.AlterModelOptions(
            name="placesave",
            options={"ordering": ["id"], "verbose_name_plural": "플레이스 저장하기 슬롯 관리"},
        ),
        migrations.AddField(
            model_name="placeclick",
            name="slot_status",
            field=models.CharField(
                blank=True,
                choices=[("대기", "대기"), ("진행", "진행"), ("중지", "중지"), ("종료", "종료")],
                default="SLOT_STATUS",
                max_length=6,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="placekeep",
            name="slot_status",
            field=models.CharField(
                blank=True,
                choices=[("대기", "대기"), ("진행", "진행"), ("중지", "중지"), ("종료", "종료")],
                default="SLOT_STATUS",
                max_length=6,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="placesave",
            name="slot_status",
            field=models.CharField(
                blank=True,
                choices=[("대기", "대기"), ("진행", "진행"), ("중지", "중지"), ("종료", "종료")],
                default="SLOT_STATUS",
                max_length=6,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="placekeep",
            name="day_count",
            field=models.CharField(
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
        migrations.AlterField(
            model_name="placesave",
            name="day_count",
            field=models.CharField(
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
    ]
