# Generated by Django 3.0.4 on 2020-03-09 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20200308_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
    ]
