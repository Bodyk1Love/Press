# Generated by Django 2.2.5 on 2020-03-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telegram_chat_id',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]