# Generated by Django 3.1.7 on 2021-04-19 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20210412_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bb',
            old_name='rubric_id',
            new_name='rubric',
        ),
    ]
