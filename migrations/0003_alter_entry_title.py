# Generated by Django 4.1.6 on 2024-05-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diary", "0002_rename_entry_entry_content_remove_entry_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="title",
            field=models.CharField(default="Untitled", max_length=200),
        ),
    ]
