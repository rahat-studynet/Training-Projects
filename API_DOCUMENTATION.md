# API Documentation

# Automated Product & Cart Management System API

This document explains the API endpoints used in the Automated Product & Cart Management System.

The API is built using Django REST Framework. It is mainly used for Postman testing and works with the `CartItem` model.

---

# Base URL

Local development base URL:

    http://127.0.0.1:8000/

API base URL:

    http://127.0.0.1:8000/api/cart/

Main endpoint:

    http://127.0.0.1:8000/api/cart/items/

---

# Authentication

The API uses Token Authentication.

Every API request must include this header:

    Authorization: Token YOUR_TOKEN_HERE

Example:

    Authorization: Token abc123yourtoken

For POST, PUT, and PATCH requests, use this header also:

    Content-Type: application/json

---

# How to Create API Token

## Option 1: Create Token from Django Admin

Go to:

    http://127.0.0.1:8000/admin/

Then:

    Tokens
    Add Token
    Select user
    Save
    Copy token key

---

## Option 2: Create Token from Django Shell

Run:

    python manage.py shell

Then run:

    from django.contrib.auth.models import User
    from rest_framework.authtoken.models import Token

    user = User.objects.get(username="admin")
    token, created = Token.objects.get_or_create(user=user)

    print(token.key)

Exit shell:

    exit()

---

# API Model

The API uses the `CartItem` model.

## CartItem Fields

| Field | Type | Description |
| ----- | ---- | ----------- |
| id | Integer | Auto-generated database ID |
| product_id | Integer | Unique product ID |
| product_name | String | Product name |
| quantity | Integer | Product quantity |
| price | Decimal | Product price |
| created_at | DateTime | Item creation date and time |

---

# API Endpoints Summary

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/cart/items/` | Get all API cart items |
| POST | `/api/cart/items/` | Create a new API cart item |
| GET | `/api/cart/items/<id>/` | Get a single API cart item |
| PUT | `/api/cart/items/<id>/` | Fully update an API cart item |
| PATCH | `/api/cart/items/<id>/` | Partially update an API cart item |
| DELETE | `/api/cart/items/<id>/` | Delete an API cart item |

---

# 1. Get All Cart Items

## Method

    GET

## URL

    http://127.0.0.1:8000/api/cart/items/

## Headers

    Authorization: Token YOUR_TOKEN_HERE

## Success Response

Status code:

    200 OK

Example response:

    []

If items exist:

{
  "id": 1,
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00",
  "created_at": "2026-07-15T10:00:00Z"
}

---

# 2. Create New Cart Item

## Method

    POST

## URL

    http://127.0.0.1:8000/api/cart/items/

## Headers

    Authorization: Token YOUR_TOKEN_HERE
    Content-Type: application/json

## Request Body

{
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00"
}

## Success Response

Status code:

    201 Created

Example response:

{
  "id": 1,
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00",
  "created_at": "2026-07-15T10:00:00Z"
}

---

# 3. Get Single Cart Item

## Method

    GET

## URL

    http://127.0.0.1:8000/api/cart/items/1/

## Headers

    Authorization: Token YOUR_TOKEN_HERE

## Success Response

Status code:

    200 OK

Example response:

{
  "id": 1,
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00",
  "created_at": "2026-07-15T10:00:00Z"
}

---

# 4. Fully Update Cart Item

PUT is used to fully update an existing item.

## Method

    PUT

## URL

    http://127.0.0.1:8000/api/cart/items/1/

## Headers

    Authorization: Token YOUR_TOKEN_HERE
    Content-Type: application/json

## Request Body

{
  "product_id": 101,
  "product_name": "Smart Watch Updated",
  "quantity": 3,
  "price": "2600.00"
}

## Success Response

Status code:

    200 OK

Example response:

{
  "id": 1,
  "product_id": 101,
  "product_name": "Smart Watch Updated",
  "quantity": 3,
  "price": "2600.00",
  "created_at": "2026-07-15T10:00:00Z"
}

---

# 5. Partially Update Cart Item

PATCH is used to update only selected fields.

## Method

    PATCH

## URL

    http://127.0.0.1:8000/api/cart/items/1/

## Headers

    Authorization: Token YOUR_TOKEN_HERE
    Content-Type: application/json

## Request Body

{
  "quantity": 5
}

## Success Response

Status code:

    200 OK

Example response:

{
  "id": 1,
  "product_id": 101,
  "product_name": "Smart Watch Updated",
  "quantity": 5,
  "price": "2600.00",
  "created_at": "2026-07-15T10:00:00Z"
}

---

# 6. Delete Cart Item

## Method

    DELETE

## URL

    http://127.0.0.1:8000/api/cart/items/1/

## Headers

    Authorization: Token YOUR_TOKEN_HERE

## Success Response

Status code:

    204 No Content

After deleting, the item will be removed from the database.

---

# Validation Rules

The API validates the following rules:

| Field | Rule |
| ----- | ---- |
| product_id | Must be unique |
| product_name | Cannot be empty |
| quantity | Must be at least 1 |
| price | Must be greater than 0 |

---

# Example Validation Error

If the same `product_id` is used again, the API returns:

{
  "success": false,
  "error": "Validation Error.",
  "details": {
    "product_id": [
      "This product already exists in your cart. Try updating its quantity instead."
    ]
  },
  "suggestion": "Please check product_id, product_name, quantity, and price."
}

---

# Authentication Error

If token is missing, the API returns:

{
  "success": false,
  "error": "Authentication Error.",
  "details": {
    "detail": "Authentication credentials were not provided."
  },
  "suggestion": "Please login or provide a valid authentication token."
}

---

# Not Found Error

If the requested item does not exist, the API returns:

{
  "success": false,
  "error": "Cart item not found.",
  "details": {
    "detail": "No CartItem matches the given query."
  },
  "suggestion": "The requested item ID does not exist in the database."
}

---

# Wrong URL Error

If the API URL is incorrect, the system returns:

{
  "success": false,
  "error": "URL Syntax Error or Missing Trailing Slash.",
  "details": "The path '/wrong-url/' does not match any valid endpoint.",
  "suggestion": "Please verify your endpoint path and make sure it ends with slash (/). Example: /api/cart/items/5/"
}

---

# API Flow

The API works in the following order:

    Postman Request
    Token Authentication
    agent_system/urls.py
    cart/urls.py
    DRF Router
    CartItemViewSet
    CartItemSerializer
    CartItem Model
    Database
    JSON Response

---

# Important Files Related to API

| File | Purpose |
| ---- | ------- |
| cart/models.py | Contains the CartItem model |
| cart/serializers.py | Converts CartItem model data to JSON and validates request data |
| cart/views.py | Contains CartItemViewSet |
| cart/urls.py | Creates API routes using DRF router |
| cart/exceptions.py | Handles custom API error responses |
| agent_system/urls.py | Connects `/api/cart/` route to cart app |
| agent_system/settings.py | Contains DRF authentication, permission, and exception handler settings |

---

# Postman Testing Checklist

| Test | Status |
| ---- | ------ |
| GET all items | Working |
| POST create item | Working |
| GET single item | Working |
| PUT full update | Working |
| PATCH partial update | Working |
| DELETE item | Working |
| Token authentication | Working |
| Validation error response | Working |
| Wrong URL response | Working |

---

# Conclusion

This API allows authenticated users to create, view, update, partially update, and delete cart item records using Django REST Framework. The API is protected with Token Authentication and includes custom error handling for better debugging and testing through Postman.