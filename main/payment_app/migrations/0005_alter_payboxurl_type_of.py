# Generated by Django 4.2 on 2023-04-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0004_rename_urls_payboxurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payboxurl',
            name='type_of',
            field=models.CharField(choices=[('Up', 'Up'), ('Pro', 'Pro'), ('Ultra', 'Ultra')], max_length=20),
        ),
    ]
