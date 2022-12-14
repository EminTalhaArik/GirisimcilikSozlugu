from django.contrib import admin

class AdminSite(admin.AdminSite):
    admin.AdminSite.site_header="Girişimcilik Sözlüğü Yönetim Paneli"
    admin.AdminSite.site_title="Girişimcilik Sözlüğü Yönetim Paneli"
