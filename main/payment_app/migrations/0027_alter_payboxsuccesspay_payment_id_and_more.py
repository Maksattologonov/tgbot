# Generated by Django 4.2.1 on 2023-05-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0026_remove_temporaryaccess_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payboxsuccesspay',
            name='payment_id',
            field=models.IntegerField(unique=True, verbose_name='ID оплаты'),
        ),
        migrations.AlterField(
            model_name='payboxsuccesspay',
            name='signature',
            field=models.CharField(unique=True, verbose_name='Подпись продукта'),
        ),
    ]
