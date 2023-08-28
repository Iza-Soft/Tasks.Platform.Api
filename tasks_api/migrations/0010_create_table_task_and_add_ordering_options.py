# Generated by Django 4.1.7 on 2023-03-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_api', '0009_rename_fields_created_updated_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'task',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='workspace',
            options={'ordering': ['-created_at']},
        ),
    ]