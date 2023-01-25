from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Feedback, FeedbackAdmin)
