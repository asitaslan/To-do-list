# Generated by Django 3.2 on 2021-04-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_remove_items_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]