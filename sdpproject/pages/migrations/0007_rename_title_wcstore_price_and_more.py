# Generated by Django 4.1.7 on 2023-04-30 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_wcstore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wcstore',
            old_name='title',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='wcstore',
            name='description',
        ),
        migrations.RemoveField(
            model_name='wcstore',
            name='image',
        ),
    ]
