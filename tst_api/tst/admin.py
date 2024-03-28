from django.contrib import admin
from .models import Tst, Page

class SayfaInline(admin.TabularInline):
    model = Page
    extra = 1 

class TstAdmin(admin.ModelAdmin):
    inlines = [SayfaInline]

admin.site.register(Tst, TstAdmin)
admin.site.register(Page)

from django.contrib import admin
from .models import MyModel
from tinymce.widgets import TinyMCE
from django.db import models

class MyModelAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinymce_init.js',)

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(
            attrs={'cols': 80, 'rows': 30},
            mce_attrs={
                'plugins': "image link paste contextmenu textpattern autolink",
                'toolbar': "undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
            }
        )},
    }


admin.site.register(MyModel, MyModelAdmin)
