# Generated by Django 4.1.7 on 2023-03-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_api', '0007_make_update_filed_to_be_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]