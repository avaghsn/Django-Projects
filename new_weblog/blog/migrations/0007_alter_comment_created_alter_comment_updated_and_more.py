# Generated by Django 5.1.7 on 2025-03-30 13:23

import django.utils.timezone
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]
