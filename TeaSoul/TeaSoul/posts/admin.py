from django.contrib import admin

# Register your models here.
# modele musimy zaimportować
from .models import Category, Post, Topic

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'topic_with_category',
        'created_by',
        'created_at',
        'updated_at',
        'text_preview',
    )
    readonly_fields = ('created_at',)
    list_filter = ('topic', 'topic__category', 'created_by')
    search_fields = ('title', 'topic__title', 'topic__category__name')
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='Topic (Category)')
    def topic_with_category(self, obj: Post) -> str:
        return f"{obj.topic.title} ({obj.topic.category.name})"

    def text_preview(self, obj: Post) -> str:
        words = obj.text.split()
        preview = ' '.join(words[:5])
        return f"{preview}..." if len(words) > 5 else preview

    text_preview.short_description = 'Text preview'
