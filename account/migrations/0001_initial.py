# Generated by Django 4.1.4 on 2023-03-07 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(default='STANDARD', max_length=100)),
                ('account_status', models.CharField(default='ACTIVE', max_length=100)),
                ('date_of_birth', models.DateField()),
                ('whatsapp_enabled_phone_number', models.CharField(max_length=15)),
                ('home_address', models.CharField(max_length=100)),
                ('balance', models.FloatField(default=0.0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'myusers',
            },
        ),
    ]
