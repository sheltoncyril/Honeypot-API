# Generated by Django 3.1.2 on 2020-12-07 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20201208_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honeypot',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]