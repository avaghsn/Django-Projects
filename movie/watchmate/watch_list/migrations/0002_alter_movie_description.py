# Generated by Django 5.1 on 2025-04-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
