from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category, Route


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Route)
class PostAdmin(admin.ModelAdmin):
    """
    Админ-панель модели маршрутов
    """
    prepopulated_fields = {'slug': ('title',)}
