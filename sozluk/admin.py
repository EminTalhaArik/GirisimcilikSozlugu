from django.contrib import admin
from .models import Term, Category
from sozluk.admin_site import AdminSite
    
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active")
    list_editable = ("is_active","category")
    search_fields = ("title","discription")
    list_filter = ("category","is_active")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
