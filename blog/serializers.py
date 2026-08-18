from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'created_date', 'published_date']

# class PostSerializer(serializers.Serializer):
#     author_id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200, required=True, allow_blank=False)
#     text = serializers.CharField(required=True, allow_blank=False)
#     created_date = serializers.DateTimeField()
#     published_date = serializers.DateTimeField(allow_null=True, required=False)

#     def create(self, validated_data):
#         """
#         Create and return a new `Post` instance, given the validated data.
#         """
#         return Post.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Post` instance, given the validated data.
#         """
#         instance.author_id = validated_data.get('author_id', instance.author_id)
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.created_date = validated_data.get('created_date', instance.created_date)
#         instance.published_date = validated_data.get('published_date', instance.published_date)
#         instance.save()
#         return instance