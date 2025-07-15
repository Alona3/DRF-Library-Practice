import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from library.models import Book, Borrowing

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def book():
    return Book.objects.create(title="Test Book", inventory=5)

@pytest.mark.django_db
def test_borrow_decreases_inventory(api_client, book):
    borrow_url = reverse('borrowing-borrow', args=[book.id])
    
    response = api_client.post(borrow_url)
    assert response.status_code == 200
    book.refresh_from_db()
    assert book.inventory == 4

@pytest.mark.django_db
def test_return_increases_inventory(api_client, book):
    borrowing = Borrowing.objects.create(book=book, user=None)
    book.inventory -= 1
    book.save()
    
    return_url = reverse('borrowing-return', args=[borrowing.id])
    
    response = api_client.post(return_url)
    assert response.status_code == 200
    book.refresh_from_db()
    assert book.inventory == 5
