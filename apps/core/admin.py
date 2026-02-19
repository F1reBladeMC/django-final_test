from django.contrib import admin
from apps.core.models import SiteInfo
# Register your models here.
@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_number', 'email')
    search_fields = ('title', 'phone_number', 'email')
    