# Generated by Django 5.0.2 on 2024-02-25 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='User',
        ),
    ]
