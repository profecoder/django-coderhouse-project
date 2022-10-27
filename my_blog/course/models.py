from django.db import models
from ckeditor.fields import RichTextField


class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Course: {self.name} | code: {self.code}"


class Homework(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()

    def __str__(self):
        return f"{self.name} | fecha: {self.due_date}"
