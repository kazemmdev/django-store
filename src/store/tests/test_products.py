import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_product_list_returns_200():
    client = APIClient()
    url = reverse('product-list')
    response = client.get(url)
    assert response.status_code == 200
