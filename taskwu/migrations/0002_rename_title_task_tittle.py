# Generated by Django 5.0.3 on 2024-03-23 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskwu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='tittle',
        ),
    ]
