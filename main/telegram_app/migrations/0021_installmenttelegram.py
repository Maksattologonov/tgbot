# Generated by Django 4.2.1 on 2023-05-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_app', '0020_remove_contactustelegram_bot_token_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstallmentTelegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст для программы рассрочки')),
                ('manager_id', models.IntegerField(verbose_name='Телеграм ID менеджера')),
            ],
            options={
                'verbose_name': 'Сообщение связаться с нами',
                'verbose_name_plural': 'Сообщение связаться с нами',
            },
        ),
    ]
