# Generated by Django 5.1.3 on 2024-11-25 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="grade",
            name="student",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="grades",
                to="main.student",
            ),
            preserve_default=False,
        ),
    ]
