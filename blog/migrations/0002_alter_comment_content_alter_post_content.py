# Generated by Django 4.2.7 on 2024-05-28 13:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
