# Generated by Django 3.1.2 on 2020-12-06 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_triggers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Triggers',
            new_name='Trigger',
        ),
        migrations.RenameField(
            model_name='trigger',
            old_name='src_ip',
            new_name='source_ip',
        ),
    ]