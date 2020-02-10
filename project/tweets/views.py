from rest_framework import filters, viewsets, permissions
from rest_framework.serializers import Serializer
from url_filter.integrations.drf import DjangoFilterBackend
from django.db.models.query import QuerySet
from django.core.exceptions import ValidationError

from project.permissions import ActionBasedPermission
from project.tweets.serializers import TweetSerializer
from project.tweets.models import Tweet


class TweetsViewset(viewsets.ModelViewSet):
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filter_fields = "__all__"
    permission_classes = (ActionBasedPermission,)
    pagination_class = None
    action_permissions = {
        permissions.IsAuthenticated: [
            "update",
            "partial_update",
            "destroy",
        ],
        permissions.AllowAny: ["create", "list", "retrieve"],
    }

    def get_serializer_class(self) -> Serializer:
        return TweetSerializer

    def get_queryset(self) -> QuerySet:
        tweets = Tweet.objects.filter(approved=True)
        return tweets
