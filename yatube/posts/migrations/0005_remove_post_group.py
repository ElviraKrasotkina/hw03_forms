# Generated by Django 2.2.6 on 2023-03-02 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230302_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
    ]