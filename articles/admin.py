from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


@admin.register(ArticleModel)
class ArticleModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

