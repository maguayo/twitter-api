from django.urls import include, path
from rest_framework.routers import DefaultRouter
from project.tweets.views import TweetsViewset


router = DefaultRouter()
router.register(r"tweets", TweetsViewset, basename="tweets")

urlpatterns = [
    path("", include(router.urls)),
]
