from django.contrib import admin
from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'status',
                    'content', 'user', 'created_at', 'update']
    list_display_links = ['slug']
    list_filter = ['created_at', 'update', 'status']
    list_editable = ['title', 'content', 'user', 'status']
    prepopulated_fields = {
        "slug": ["title"]
    }
