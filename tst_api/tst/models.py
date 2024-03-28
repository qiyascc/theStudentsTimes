from django.db import models
import calendar
from tinymce.models import HTMLField

class Tst(models.Model):
    editor = models.CharField(max_length=100, default='Bayram Bayramov')
    cover = models.ImageField(upload_to='cover/%Y/%m/')
    month = models.DateField()

    def __str__(self):
        month_name = calendar.month_name[self.month.month]
        return f"{self.month.year} - {month_name}"

class Page(models.Model):
    Tst = models.ForeignKey(Tst, related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    document = models.FileField(upload_to='document/%Y/%m/')

    def __str__(self):
        return self.title



class MyModel(models.Model):
    content = HTMLField()