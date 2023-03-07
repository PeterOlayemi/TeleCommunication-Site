# Generated by Django 4.1.4 on 2023-03-07 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CablePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=299)),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Checker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=299)),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=299)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='With',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queried', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField()),
                ('charge', models.PositiveIntegerField(default=50)),
                ('status', models.CharField(default='Processing', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=99)),
                ('amount', models.PositiveIntegerField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.service')),
            ],
        ),
        migrations.CreateModel(
            name='Elect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('queried', models.BooleanField(default=False)),
                ('name', models.CharField(default='Electricity', max_length=100)),
                ('status', models.CharField(default='Processing', max_length=100)),
                ('meter_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
                ('recharge_now', models.BooleanField(default=True)),
                ('schedule_for_later', models.BooleanField(default=False)),
                ('one_off', models.BooleanField(default=True)),
                ('auto_renew', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.electservice')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('queried', models.BooleanField(default=False)),
                ('name', models.CharField(default='Education', max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('status', models.CharField(default='Processing', max_length=100)),
                ('service', models.IntegerField(choices=[(1, 'WAEC RESULT CHECKER = #5000'), (2, 'NECO RESULT CHECKER = #2000')], default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quantity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.checker')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('queried', models.BooleanField(default=False)),
                ('status', models.CharField(default='Processing', max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('recharge_now', models.BooleanField(default=True)),
                ('schedule_for_later', models.BooleanField(default=False)),
                ('one_off', models.BooleanField(default=True)),
                ('auto_renew', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.plan')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.service')),
            ],
        ),
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('queried', models.BooleanField(default=False)),
                ('name', models.CharField(default='Cable TV', max_length=100)),
                ('card_number', models.CharField(max_length=30)),
                ('status', models.CharField(default='Processing', max_length=100)),
                ('service', models.IntegerField(verbose_name=((1, 'DSTV'), (2, 'GOTV'), (3, 'STARTIMES')))),
                ('choose_type', models.IntegerField(choices=[(1, 'Renew Subscription'), (2, 'Change Subscription')], default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('recharge_now', models.BooleanField(default=True)),
                ('schedule_for_later', models.BooleanField(default=False)),
                ('one_off', models.BooleanField(default=True)),
                ('auto_renew', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.cableplan')),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.BooleanField(default=False)),
                ('bank_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=10)),
                ('account_name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Poor', 'Poor'), ('Excellent', 'Excellent'), ('Unavailable', 'Unavailable')], default='Poor', max_length=99)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.service')),
            ],
        ),
        migrations.CreateModel(
            name='Airtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('queried', models.BooleanField(default=False)),
                ('status', models.CharField(default='Processing', max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('choose_network', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.service')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]