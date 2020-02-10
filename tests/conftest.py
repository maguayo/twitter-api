import pytest
import json
from django.test import Client
from django.urls import reverse
from rest_framework import status


@pytest.fixture
@pytest.mark.django_db
def setup_tests():
    pass