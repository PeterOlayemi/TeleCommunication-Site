# Generated by Django 4.1.4 on 2023-03-06 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_myuser_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='balance',
        ),
    ]