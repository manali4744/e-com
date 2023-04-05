from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
# Register your models here.
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('id', 'phone', 'name', 'is_admin', 'is_valid')
    # inlines = [CardDetailInline]
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('name','email','is_valid')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'name', 'password1', 'password2',),
        }),
    )

    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Customer)
