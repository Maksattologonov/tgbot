# Generated by Django 4.2 on 2023-04-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0002_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='type_of',
            field=models.CharField(choices=[('up', 'Front-end'), ('pro', 'Back-end'), ('ultra', 'Design')], max_length=20),
        ),
    ]