# Generated by Django 4.1b1 on 2022-07-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slot", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slot",
            name="slot_start_date",
            field=models.DateField(),
        ),
    ]
