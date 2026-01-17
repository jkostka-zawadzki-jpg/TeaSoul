from rest_framework import serializers
from .models import Category, Topic, Post


class TopicSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.save()
    #     return instance

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        # musimy wskazać klasę modelu
        model = Category
        # definiując poniższe pole możemy określić listę właściwości modelu,
        # które chcemy serializować
        fields = ['id', 'name', 'description']
        # definicja pola modelu tylko do odczytu
        read_only_fields = ['id']

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        # musimy wskazać klasę modelu
        model = Post
        # definiując poniższe pole możemy określić listę właściwości modelu,
        # które chcemy serializować
        fields = ['id', 'title', 'text', 'topic', 'slug', 'created_at', 'updated_at', 'created_by']
        # definicja pola modelu tylko do odczytu
        read_only_fields = ['id']