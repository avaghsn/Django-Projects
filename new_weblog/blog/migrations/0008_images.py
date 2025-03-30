# Generated by Django 5.1.7 on 2025-03-30 19:28

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_created_alter_comment_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ انتشار')),
                ('image_file', models.ImageField(upload_to='post_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.post', verbose_name='تص اویر')),
            ],
        ),
    ]
