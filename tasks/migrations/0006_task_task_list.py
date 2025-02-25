# Generated by Django 4.2.5 on 2024-10-06 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_remove_task_task_list"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="task_list",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="tasks.tasklist",
            ),
            preserve_default=False,
        ),
    ]
