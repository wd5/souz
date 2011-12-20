from django.contrib import admin
from production.models import Production

class ProductionPageAdmin(admin.ModelAdmin):
    admin.site.register(Production)
