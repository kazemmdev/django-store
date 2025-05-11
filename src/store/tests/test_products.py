import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from store.models import Product


@pytest.mark.django_db
def test_product_list_returns_200():
    Product.objects.create(name='Test Product', price=10.99)

    client = APIClient()
    url = reverse('product-list')
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]['name'] == 'Test Product'
    assert data[0]['price'] == '10.99'


@pytest.mark.django_db
def test_create_product_returns_201_and_saves_product():
    client = APIClient()
    url = reverse('product-list')

    payload = {
        'name': 'Test Product',
        'price': '10.99',
    }

    response = client.post(url, data=payload, format='json')
    assert response.status_code == 201
    assert Product.objects.filter(name='Test Product').exists()

@pytest.mark.django_db
def test_create_product_returns_409():
    client = APIClient()
    url = reverse('product-list')
    payload = {}
    response = client.post(url, data=payload, format='json')
    assert response.status_code == 400

@pytest.mark.django_db
def test_get_single_product():
    product = Product.objects.create(name="Test Product", price=10.99)
    client = APIClient()
    url = reverse('product-detail', args=[product.id])

    response = client.get(url)

    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

@pytest.mark.django_db
def test_get_single_product_returns_404():
    client = APIClient()
    url = reverse('product-detail', args=[99])
    response = client.get(url)
    assert response.status_code == 404

@pytest.mark.django_db
def test_update_product():
    product = Product.objects.create(name="Test Product", price=10.99)
    client = APIClient()
    url = reverse('product-detail', args=[product.id])

    payload = {"name": "Test Product (Updated)", "price": "14.99"}
    response = client.put(url, payload, format="json")

    product.refresh_from_db()
    assert response.status_code == 200
    assert product.name == "Test Product (Updated)"
    assert str(product.price) == "14.99"


@pytest.mark.django_db
def test_delete_product():
    product = Product.objects.create(name="Test Product", price=10.99)
    client = APIClient()
    url = reverse('product-detail', args=[product.id])

    response = client.delete(url)

    assert response.status_code == 204
    assert not Product.objects.filter(id=product.id).exists()
