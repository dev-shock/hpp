from django.contrib import admin
from .models import Upload, Download
# Register your models here.


admin.site.register(Download)
admin.site.register(Upload, list_display=['title'])

