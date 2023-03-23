from ast import arg
from email.policy import default
from enum import unique
from secrets import choice
from django.db import models
from django.utils.text import slugify

class Category (models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Term (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="terms", null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"

