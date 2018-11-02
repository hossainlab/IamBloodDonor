from django.contrib import admin
from .models import BlogPost, Category

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['author','title','posted_on', 'updated_on', 'status']
    list_editable = ['status']
    list_filter = ['posted_on','updated_on', 'status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
admin.site.register(Category, CategoryAdmin)