# Generated by Django 3.2 on 2021-04-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_items_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lists',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
