from django.contrib import admin
from .models import Term, Category
from sozluk.admin_site import AdminSite
from import_export.admin import ImportExportModelAdmin
from .resources import TermResource
    
@admin.register(Term)
class TermAdmin(ImportExportModelAdmin):
    list_display = ("title", "is_active", "id")
    list_editable = ("is_active",)
    search_fields = ("title","description")
    list_filter = ("category","is_active")

    resource_class = TermResource

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
 