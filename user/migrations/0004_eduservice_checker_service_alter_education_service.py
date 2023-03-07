# Generated by Django 4.1.4 on 2023-03-07 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_cableplan_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=299)),
            ],
        ),
        migrations.AddField(
            model_name='checker',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.eduservice'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.eduservice'),
        ),
    ]