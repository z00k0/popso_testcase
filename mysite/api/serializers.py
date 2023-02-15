from rest_framework import serializers
from news.models import Channel, Post


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["name"]


class PostListSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["tg_id", "text", "posted_at", "image", "channel"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["channel"] = ChannelSerializer(instance.channel_id).data
        return ret
