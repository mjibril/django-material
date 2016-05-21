from django.contrib import admin
from . import models


@admin.register(models.Issue29)
class Issue29Admin(admin.ModelAdmin):
    fields = ('id', 'modified', 'content')
    readonly_fields = ('id', 'modified', )
