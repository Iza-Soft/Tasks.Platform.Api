# Generated by Django 4.1.7 on 2023-03-22 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_api', '0004_add_progress_field_in_workspacetable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workspace',
            old_name='progess',
            new_name='progress',
        ),
    ]