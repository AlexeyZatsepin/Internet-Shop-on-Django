from django.contrib import admin

admin.AdminSite.site_header = 'the best web shop admin panel'

from catalog.models import *


class SmartPhoneAdmin(admin.ModelAdmin):
    list_display = ['product_title', 'operating_system']
    ordering = ['product_title']
    list_filter = ['operating_system']
    search_fields = ['product_distributor']


class NoteBookAdmin(admin.ModelAdmin):
    list_display = ['product_title', 'operating_system']


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(SmartPhone, SmartPhoneAdmin)
admin.site.register(TV)
admin.site.register(Notebook, NoteBookAdmin)
admin.site.register(FlashMemory)
