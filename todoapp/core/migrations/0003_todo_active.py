# Generated by Django 4.1.2 on 2023-08-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_todo_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]
