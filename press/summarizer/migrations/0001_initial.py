# Generated by Django 2.2.5 on 2020-03-09 17:44

import datetime
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
            name='SavedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField(default=None)),
                ('summarized_text', models.TextField(default=None)),
                ('number_of_summarized_sentences', models.IntegerField(default=None)),
                ('datetime_of_creation', models.DateTimeField(default=datetime.datetime.now)),
                ('word_difference', models.IntegerField(default=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_premium', models.BooleanField(default=False)),
                ('summarized_texts', models.IntegerField(default=0)),
                ('summarized_words', models.IntegerField(default=0)),
                ('telegram_chat_id', models.CharField(default=None, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
