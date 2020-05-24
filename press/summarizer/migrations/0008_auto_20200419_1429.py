# Generated by Django 2.2.5 on 2020-04-19 14:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('summarizer', '0007_auto_20200405_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='telegram_chat_id',
        ),
        migrations.AlterField(
            model_name='savedtext',
            name='datetime_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 14, 29, 22, 899940)),
        ),
        migrations.CreateModel(
            name='TelegramProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('activation_code', models.CharField(blank=True, default=None, max_length=50, null=True, unique=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
