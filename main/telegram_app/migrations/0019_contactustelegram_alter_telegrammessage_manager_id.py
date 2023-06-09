# Generated by Django 4.2.1 on 2023-05-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_app', '0018_alter_telegrammessage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsTelegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_token', models.CharField(max_length=255, verbose_name='Токен телеграм бота')),
                ('text', models.TextField(verbose_name='Текст')),
                ('manager_id', models.IntegerField(verbose_name='Телеграм ID менеджера')),
            ],
            options={
                'verbose_name': 'Сообщение связаться с нами',
                'verbose_name_plural': 'Сообщение связаться с нами',
            },
        ),
        migrations.AlterField(
            model_name='telegrammessage',
            name='manager_id',
            field=models.IntegerField(verbose_name='Телеграм ID менеджера'),
        ),
    ]
