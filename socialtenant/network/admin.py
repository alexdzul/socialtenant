from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "created_by", "timestamp")
    search_fields = ["content", "created_by__first_name", "craeted_by__last_name",
                     "created_by__username", "created_by__email"]
