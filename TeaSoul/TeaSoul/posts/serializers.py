from rest_framework import serializers

from .models import Category, Post, Topic


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id"]


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name", "category", "created"]
        read_only_fields = ["id", "created"]


class PostSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField()

    def get_created_by_name(self, obj):
        full_name = obj.created_by.get_full_name()
        return full_name if full_name else obj.created_by.username

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "text",
            "topic",
            "slug",
            "created_at",
            "updated_at",
            "created_by",
            "created_by_name",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "created_by", "created_by_name"]
