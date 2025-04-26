from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import Manager, VisaDirection, Testimonial, ContactMessage, SiteConfiguration


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'phone', 'email', 'order', 'display_photo']
    list_editable = ['order']
    search_fields = ['name', 'position', 'email']
    
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.photo.url)
        return "—"
    display_photo.short_description = _("Фото")


@admin.register(VisaDirection)
class VisaDirectionAdmin(admin.ModelAdmin):
    list_display = ['country_name', 'order', 'display_flag']
    list_editable = ['order']
    search_fields = ['country_name']
    
    def display_flag(self, obj):
        if obj.flag:
            return format_html('<img src="{}" width="40" height="25" />', obj.flag.url)
        return "—"
    display_flag.short_description = _("Флаг")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'rating', 'date_added', 'is_active', 'order', 'display_photo']
    list_editable = ['is_active', 'order']
    list_filter = ['rating', 'is_active', 'date_added']
    search_fields = ['client_name', 'text']
    
    def display_photo(self, obj):
        if obj.client_photo:
            return format_html('<img src="{}" width="40" height="40" style="border-radius: 50%;" />', obj.client_photo.url)
        return "—"
    display_photo.short_description = _("Фото")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_sent', 'is_processed']
    list_editable = ['is_processed']
    list_filter = ['is_processed', 'date_sent']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['name', 'email', 'phone', 'message', 'date_sent']
    
    def has_add_permission(self, request):
        return False


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Основная информация"), {
            'fields': ('site_name', 'site_slogan', 'about_text')
        }),
        (_("Контактная информация"), {
            'fields': ('address', 'email', 'phone')
        }),
        (_("Социальные сети"), {
            'fields': ('whatsapp', 'telegram', 'instagram')
        }),
    )
    
    def has_add_permission(self, request):
        # Запрещает создание дополнительных конфигураций
        return not SiteConfiguration.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Запрещает удаление конфигурации
        return False