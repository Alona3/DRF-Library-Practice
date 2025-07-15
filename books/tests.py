from rest_framework.test import APIClient
from django.contrib.auth.models import User
import pytest
from django.urls import reverse

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def admin_user():
    return User.objects.create_superuser('admin', 'admin@test.com', 'pass123')

@pytest.fixture
def regular_user():
    return User.objects.create_user('user', 'user@test.com', 'pass123')

@pytest.mark.django_db
def test_admin_can_create_book(api_client, admin_user):
    api_client.force_authenticate(admin_user)
    url = reverse('book-list')
    data = {"title": "New Book", "inventory": 10}
    response = api_client.post(url, data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_regular_user_cannot_create_book(api_client, regular_user):
    api_client.force_authenticate(regular_user)
    url = reverse('book-list')
    data = {"title": "New Book", "inventory": 10}
    response = api_client.post(url, data)
    assert response.status_code == 403
