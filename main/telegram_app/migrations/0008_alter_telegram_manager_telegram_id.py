# Generated by Django 4.2 on 2023-05-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_app', '0007_remove_telegram_manager_telegram_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegram',
            name='manager_telegram_id',
            field=models.IntegerField(verbose_name='ID группы с менеджером телеграм'),
        ),
    ]
