# 🛒 Simple Store API

A clean and test-driven REST API for an online store built with **Django**, **Django REST Framework**, and **Docker Compose**.

This project follows the **TDD (Test-Driven Development)** approach and supports full CRUD operations for `Product` resources.

---

## 🚀 Features

- Django 5.x + DRF
- RESTful CRUD for Products
- Fully containerized with Docker Compose
- TDD setup with `pytest`
- Simple Makefile-based workflow
- MySQL-backed data persistence

---

## 🧱 Project Structure

```
.
├── src/                 
│   ├── backend/         # Django project
│   └── store/           # App for managing products
├── docker-compose.yml
├── Makefile             # Developer commands
├── requirements.txt
└── .env
```

---

## 🐳 Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [GNU Make](https://www.gnu.org/software/make/)

---

## ⚙️ Setup & Run

### 🔧 Environment

Create a `.env` file:

```env
DB_NAME=store_db
DB_USER=store_user
DB_PASSWORD=store_pass
DB_ROOT_PASSWORD=rootpass
DJANGO_SETTINGS_MODULE=backend.settings
```

---

### 🚀 Start the App

```bash
make compose
```

This will:
- Stop and remove any old containers
- Rebuild everything
- Start the application on [http://localhost:8000](http://localhost:8000)

---

### ✅ Run Tests

```bash
make test
```

Runs the test suite using `pytest` inside the container.

---

## 🧪 API Endpoints

All endpoints are prefixed with `/api/`.

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| GET    | `/products/`       | List all products   |
| POST   | `/products/`       | Create a product    |
| GET    | `/products/<id>/`  | Get single product  |
| PUT    | `/products/<id>/`  | Update a product    |
| DELETE | `/products/<id>/`  | Delete a product    |

---

## 🔍 Example Product Payload

```json
{
  "name": "Laptop",
  "price": "999.99"
}
```

---

## 🧪 TDD Style

All features are written starting from tests first using `pytest` + Django DB fixtures.

Example:

```python
def test_create_product():
    response = client.post('/api/products/', {"name": "Phone", "price": "499.99"})
    assert response.status_code == 201
```

---

## 👨‍💻 Developer Workflow

- Edit code → `make compose`
- Write a failing test → `make test`
- Make it pass → commit!
- Repeat 💡

---

## 📦 Tech Stack

- Python 3.10
- Django 5.x
- Django REST Framework
- MySQL 8
- Pytest
- Docker Compose
- Makefile

---

## 📝 License

MIT — Use it freely, improve it responsibly.
