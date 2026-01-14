from django.contrib import admin

# Register your models here.
# modele musimy zaimportować
from .models import Category, Post, Topic

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'created_by', 'created_at', 'updated_at', 'text_preview')
    readonly_fields = ('created_at',)

    def text_preview(self, obj: Post) -> str:
        words = obj.text.split()
        preview = ' '.join(words[:5])
        return f"{preview}..." if len(words) > 5 else preview

    text_preview.short_description = 'Text preview'
