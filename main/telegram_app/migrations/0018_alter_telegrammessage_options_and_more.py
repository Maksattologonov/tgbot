# Generated by Django 4.2.1 on 2023-05-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_app', '0017_telegrammessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegrammessage',
            options={'verbose_name': 'Сообщение телеграм бота', 'verbose_name_plural': 'Сообщение телеграм бота'},
        ),
        migrations.RemoveField(
            model_name='telegrammessage',
            name='bot_id',
        ),
        migrations.AddField(
            model_name='telegrammessage',
            name='bot_token',
            field=models.CharField(default=3, max_length=255, verbose_name='Токен телеграм бота'),
            preserve_default=False,
        ),
    ]