from rest_framework import serializers
from .models import *


class NewsAgentsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAgents
        fields = "__all__"
        depth = 2


class NewsAgentsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAgents
        fields = [
            "name",
            "profile",
        ]


class NewsArticlesGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticles
        fields = "__all__"
        depth = 2


class NewsArticlesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticles
        fields = [
            "provider",
            "tittle",
            "pic1",
            "subtitle",
            "content",
            "pic2",
            "sub_content",
            "likes",
        ]


class ArticleCommentsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComments
        fields = "__all__"
        depth = 2


class ArticleCommentsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComments
        fields = [
            "user",
            "comment",
            "article",
            "likes",
        ]

