# Generated by Django 3.1.2 on 2020-12-07 22:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20201207_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='honeypot',
            name='container_port',
            field=models.PositiveIntegerField(default=80, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)]),
        ),
        migrations.AlterField(
            model_name='honeypot',
            name='container_id',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='honeypot',
            name='container_ip',
            field=models.GenericIPAddressField(default=None),
            preserve_default=False,
        ),
    ]
