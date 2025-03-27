from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


# Create your models here.

# Managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        REJECTED = 'RJ', 'Rejected'

    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts', verbose_name="نویسنده")

    # data fields
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    slug = models.SlugField(max_length=200)

    # date
    publish = jmodels.jDateTimeField(default=timezone.now(), verbose_name="تاریخ انتشار")
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)

    # choice fields
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name="وضعیت")

    objects = jmodels.jManager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.title
