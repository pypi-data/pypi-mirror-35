from django.contrib import admin
from .models import SocialNetwork
from django.conf import settings
__author__ = "spi4ka"


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    search_fields = ('name', 'link', )
    list_display = ('name', 'link',)
