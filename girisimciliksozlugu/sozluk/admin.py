from django.contrib import admin
from .models import Term, Category

class TermAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active")
    list_editable = ("is_active","category")
    search_fields = ("title","discription")
    list_filter = ("category","is_active")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

admin.site.register(Term, TermAdmin)
admin.site.register(Category, CategoryAdmin)
