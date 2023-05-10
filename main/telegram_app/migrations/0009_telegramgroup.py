# Generated by Django 4.2 on 2023-05-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_app', '0008_alter_telegram_manager_telegram_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название группы')),
                ('group_id', models.IntegerField(verbose_name='ID группы телеграма')),
            ],
            options={
                'verbose_name': 'Группа телеграм',
                'verbose_name_plural': 'Группы телеграм',
            },
        ),
    ]