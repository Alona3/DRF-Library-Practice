import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_user_registration(api_client):
    url = reverse('user-register')
    data = {
        "username": "testuser",
        "password": "testpass123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert User.objects.filter(username="testuser").exists()

@pytest.mark.django_db
def test_user_can_get_token(api_client, regular_user):
    url = reverse('token_obtain_pair')
    data = {
        "username": regular_user.username,
        "password": "pass123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_user_restrictions(api_client, regular_user):
    api_client.force_authenticate(regular_user)
    url = reverse('book-list')
    data = {"title": "Unauthorized Book", "inventory": 5}
    response = api_client.post(url, data)
    assert response.status_code == 403
