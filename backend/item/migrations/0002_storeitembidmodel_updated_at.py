# Generated by Django 5.0.3 on 2024-03-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="storeitembidmodel",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
