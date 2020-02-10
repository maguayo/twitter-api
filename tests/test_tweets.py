import pytest
import json
import jwt
from django.conf import settings
from django.test import Client
from django.urls import reverse
from rest_framework import status
from project.tweets.models import Tweet
from tests.constants import TWEET_CONTENT_LARGE, TWEET_NAME, TWEET_CONTENT

@pytest.mark.django_db
def test_creating_a_tweet_with_more_than_50_chars_fails_with_400_error():
    c = Client()

    response = c.post(
        reverse("tweets-list"),
        content_type="application/json",
        data=json.dumps({"name": TWEET_NAME, "content": TWEET_CONTENT_LARGE}),
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_create_tweet():
    c = Client()

    response = c.post(
        reverse("tweets-list"),
        content_type="application/json",
        data=json.dumps({"name": TWEET_NAME, "content": TWEET_CONTENT}),
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_list_hundreds_of_tweets_without_pagination():
    c = Client()

    # Create 200 tweets.
    tweets = []
    for _ in range(200):
        tweets.append(
            Tweet(name=TWEET_NAME, content=TWEET_CONTENT)
        )
    Tweet.objects.bulk_create(tweets)

    response = c.get(
        reverse("tweets-list"),
        content_type="application/json",
    )
        
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 200



@pytest.mark.django_db
def test_update_a_tweet_should_raise_a_401_unauthorized_error():
    c = Client()

    response = c.post(
        reverse("tweets-list"),
        content_type="application/json",
        data=json.dumps({"name": TWEET_NAME, "content": TWEET_CONTENT}),
    )

    assert response.status_code == status.HTTP_201_CREATED

    body = response.json()

    response = c.patch(
        reverse("tweets-detail", kwargs={"pk": body["id"]}),
        content_type="application/json",
        data=json.dumps({"name": TWEET_NAME, "content": TWEET_CONTENT}),
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_deleting_a_tweet_should_raise_a_401_unauthorized_error():
    c = Client()

    response = c.post(
        reverse("tweets-list"),
        content_type="application/json",
        data=json.dumps({"name": TWEET_NAME, "content": TWEET_CONTENT}),
    )

    assert response.status_code == status.HTTP_201_CREATED

    body = response.json()

    assert Tweet.objects.count() == 1

    response = c.delete(
        reverse("tweets-detail", kwargs={"pk": body["id"]}),
        content_type="application/json",
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Tweet.objects.count() == 1
