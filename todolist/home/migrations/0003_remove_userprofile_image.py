# Generated by Django 3.2 on 2021-04-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_userprofile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]
