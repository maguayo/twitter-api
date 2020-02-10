from project.tweets.models import Tweet
from rest_framework import serializers, status


class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        read_only_fields = ("id", "created")
        fields = "__all__"
