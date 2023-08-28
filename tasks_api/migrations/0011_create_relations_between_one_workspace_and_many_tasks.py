# Generated by Django 4.1.7 on 2023-03-28 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_api', '0010_create_table_task_and_add_ordering_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='workspace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks_api.workspace'),
        ),
    ]
