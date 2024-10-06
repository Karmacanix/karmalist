# Generated by Django 4.2.5 on 2024-10-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("due_date", models.DateTimeField()),
                (
                    "task_status",
                    models.CharField(
                        choices=[
                            ("TODO", "TO DO"),
                            ("INPROGRESS", "IN PROGRESS"),
                            ("COMPLETE", "COMPLETE"),
                            ("CANCEL", "CANCELLED"),
                            ("ONHOLD", "ON HOLD"),
                        ],
                        default="TODO",
                    ),
                ),
            ],
        ),
    ]