# Generated by Django 4.1rc1 on 2022-07-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("place", "0003_alter_placekeep_options_alter_placesave_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="placekeep",
            name="modyfi_check",
            field=models.BooleanField(default=False),
        ),
    ]