# Generated by Django 4.1.7 on 2023-03-28 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_api', '0019_change_field_name_from_workspace_id_id_to_workspace_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
