# Generated by Django 3.1.2 on 2020-12-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201206_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='full_log',
            field=models.TextField(blank=True),
        ),
    ]
