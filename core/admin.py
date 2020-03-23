from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

class MyUserAdmin(UserAdmin):
    fieldsets =(
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'email',
            'qualifications'
        )}),
        (('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        ),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'qualifications'
            )}
        ),
    )

@admin.register(ActionCategory)
class ActionCategoryAdmin(admin.ModelAdmin):
    model = ActionCategory
    list_display = ["name"]

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    model = Qualification
    list_display = ["name"]

@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin):
    model = Restriction
    list_display = ["name"]

@admin.register(EquipmentProvided)
class EquipmentProvidedAdmin(admin.ModelAdmin):
    model = EquipmentProvided
    list_display = ["name"]

@admin.register(EquipmentSelf)
class EquipmentSelfAdmin(admin.ModelAdmin):
    model = EquipmentSelf
    list_display = ["name"]

@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    model = PublicationCategory
    list_display = ["title"]

@admin.register(MulticastMessage)
class MulticastMessageAdmin(admin.ModelAdmin):
    model = MulticastMessage
    list_display = ["title", "posted"]

@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    model = BlogEntry

@admin.register(SentArchive)
class SentArchiveAdmin(admin.ModelAdmin):
    model = SentArchive
    readonly_fields = ['person', 'current_email', 'multicast_message']

admin.site.register(Person, MyUserAdmin)
