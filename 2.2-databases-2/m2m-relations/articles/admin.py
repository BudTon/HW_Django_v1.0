from django.contrib import admin
from .models import Article, Scope, Tag


class ScopeInline(admin.TabularInline):
    model = Scope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

