from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Page
from image_cropping import ImageCroppingMixin
from ckeditor.widgets import CKEditorWidget
from django.db import models


class PageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.register(Page, PageAdmin)
