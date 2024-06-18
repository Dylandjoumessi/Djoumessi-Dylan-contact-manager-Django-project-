from django.contrib import admin
from .models import Contact, Group

admin.site.site_header = "Contact Manager Administration"
admin.site.site_title = "Contact Manager Admin Portal"
admin.site.index_title = "Welcome to the Contact Manager Admin"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'user')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('user',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)