from django.db import models
from project.models import BaseModel


class Tweet(BaseModel):
    name = models.CharField(max_length=250)
    content = models.CharField(max_length=50)

    # In case we don't like free speech and want to censor the Tweet
    approved = models.BooleanField(default=True)

    class Meta:
        db_table = "tweets"
