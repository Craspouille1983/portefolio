# Generated by Django 5.0.7 on 2024-07-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("folio", "0006_rename_icon_contact_contact_icon_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="level",
            field=models.IntegerField(),
        ),
    ]
