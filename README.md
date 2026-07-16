# Automated Product & Cart Management System

A beginner-friendly full-stack Django and Django REST Framework (DRF) application with role-based access for admin users and regular users.

The system allows users to sign up, but newly registered users cannot access the system until an admin verifies or approves them from the Django admin panel. After approval, users can sign in. Admin users can manage products through a simple product management system, while regular users can view products, add products to cart, update quantity, remove cart items, and complete checkout.

This project also includes a DRF API system for Postman testing using Token Authentication.

---

## 🚀 Features

## User Authentication & Approval

* **Home Page:** Includes Sign Up, Sign In, and Admin Panel options.
* **User Sign Up:** New users can register using username, email, password, and confirm password.
* **Password Validation:** Checks password match, minimum length, capital letter, number, and special character.
* **Duplicate Validation:** Prevents duplicate username and duplicate email.
* **Admin Approval System:** Newly registered users are saved as `Not Verified` by default.
* **Verified User Login:** Users can sign in only after admin approval.
* **Custom Admin Panel Status:** Admin can see user verification status as `Verified` or `Not Verified`.
* **Role-Based Redirect:**
  * Admin or staff users are redirected to the admin dashboard.
  * Regular users are redirected to the product listing page.
* **Logout System:** Logged-in users can securely log out and return to the home page.

---

## Role-Based System

| User Type | Permission |
| --------- | ---------- |
| Admin / Staff User | Can access admin dashboard and product management system |
| Regular User | Can view products, add products to cart, update cart quantity, remove cart items, and checkout |
| Not Verified User | Cannot sign in until approved by admin |

---

## Admin Product Management System

Admin users can manage products from a custom CMS-style product management page.

### Admin Features

* **Admin Dashboard:** Separate dashboard for admin users.
* **Product Management Page:** Shows all added products.
* **Add Product:** Admin can add product name, description, image, price, and stock.
* **Edit Product:** Admin can update existing product details.
* **Delete Product:** Admin can remove products from the product list.
* **Product Image Upload:** Product images are uploaded using Django media file handling.
* **Stock Management:** Product stock is stored and updated after checkout.

---

## Regular User Cart & Checkout System

Regular users can use the customer-side product and cart system.

### Regular User Features

* **Product Listing Page:** Shows available products with image, description, price, and stock.
* **Add to Cart:** Users can add products to their cart.
* **Quantity Handling:** If the same product is added again, quantity is increased instead of creating duplicate rows.
* **Quantity Update:** Users can increase or decrease quantity from the cart page.
* **Stock Checking:** Users cannot add more quantity than available stock.
* **My Cart Page:** Shows cart items, quantity, item total, and grand total.
* **Remove Item:** Users can remove items from their cart.
* **Checkout:** Users can confirm checkout.
* **Stock Reduction:** Product stock is reduced after successful checkout.
* **Cart Clear After Checkout:** User cart becomes empty after checkout.

---

## DRF Cart API System

A DRF API system is also available for Postman testing.

### API Features

* **DRF ModelViewSet:** Provides list, create, retrieve, update, partial update, and delete operations.
* **Token Authentication:** API requests can be tested using DRF token authentication.
* **Session Authentication:** Browser-based authenticated API access is also supported.
* **Basic Authentication:** Basic authentication is also added for testing support.
* **Custom Exception Handler:** Returns clean error responses for authentication errors, validation errors, missing items, invalid URLs, wrong HTTP methods, and bad JSON.
* **URL Fallback Handler:** Invalid or missing-slash URLs return a structured error response.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3
* **Authentication:** Django Authentication System, DRF Token Authentication, Session Authentication, Basic Authentication
* **Admin Panel:** Django Admin
* **Image Upload:** Pillow, Django Media Files
* **API Testing Tool:** Postman

---

# 📋 Installation & Local Setup

## 1. Open the Project Folder

Go to the project folder:

    cd "Training Project Practice"

Make sure this folder contains:

* manage.py
* accounts
* cart
* agent_system
* requirements.txt

---

## 2. Set Up a Virtual Environment

Create a virtual environment:

    python -m venv .venv

### Activate the environment on Windows PowerShell

    .\.venv\Scripts\Activate.ps1

### Activate the environment on Mac/Linux

    source .venv/bin/activate

After activation, the terminal should show something like:

    (.venv)

---

## 3. Install Dependencies

Install all required packages:

    pip install -r requirements.txt

If `requirements.txt` is not available, install manually:

    pip install django djangorestframework pillow

Then create `requirements.txt`:

    pip freeze > requirements.txt

---

## 4. Run Database Migrations

Run migrations:

    python manage.py makemigrations

    python manage.py migrate

If only cart app changes are needed:

    python manage.py makemigrations cart

    python manage.py migrate

---

## 5. Create a Superuser

Create an admin account to approve users and manage products:

    python manage.py createsuperuser

Example:

    Username: admin
    Email address: admin@example.com
    Password: Admin@1234

---

## 6. Start the Development Server

Run the server:

    python manage.py runserver

The application will be accessible locally at:

    http://127.0.0.1:8000/

---

# 🔐 User Approval Workflow

## Step 1: User Sign Up

A new user goes to:

    http://127.0.0.1:8000/signup/

The user enters:

* Username
* Email
* Password
* Confirm Password

After successful signup, the account is created as:

    Not Verified

This means the user cannot sign in yet.

---

## Step 2: Admin Approval

Admin goes to:

    http://127.0.0.1:8000/admin/

Then admin can approve the user from the user list.

Admin can use the custom admin action:

    Approve selected users

After approval, the user status becomes:

    Verified

---

## Step 3: User Sign In

Approved users can sign in from:

    http://127.0.0.1:8000/signin/

After successful login:

| User Type | Redirect URL |
| --------- | ------------ |
| Admin / Staff User | http://127.0.0.1:8000/admin-dashboard/ |
| Regular User | http://127.0.0.1:8000/products/ |

---

# 👨‍💼 Admin Workflow

## Step 1: Admin Sign In

Admin signs in from:

    http://127.0.0.1:8000/signin/

After login, admin is redirected to:

    http://127.0.0.1:8000/admin-dashboard/

---

## Step 2: Admin Dashboard

Admin dashboard shows:

* Total Products
* Total Stock
* Active Cart Items
* Quick link to manage products
* Quick link to add product
* Quick link to Django Admin Panel

Dashboard URL:

    http://127.0.0.1:8000/admin-dashboard/

---

## Step 3: Manage Products

Admin can manage products from:

    http://127.0.0.1:8000/admin-products/

Admin can:

* View product list
* Add new product
* Edit product
* Delete product

---

## Step 4: Add Product

Admin can add products from:

    http://127.0.0.1:8000/admin-products/add/

Product fields:

* Product Name
* Description
* Product Image
* Price
* Stock

---

## Step 5: Edit Product

Admin can edit a product from:

    http://127.0.0.1:8000/admin-products/edit/<product_id>/

Example:

    http://127.0.0.1:8000/admin-products/edit/1/

---

## Step 6: Delete Product

Admin can delete a product from:

    http://127.0.0.1:8000/admin-products/delete/<product_id>/

Delete is handled using a POST request with CSRF protection.

---

# 🛒 Regular User Workflow

## Step 1: Regular User Sign In

Approved regular users sign in from:

    http://127.0.0.1:8000/signin/

After login, regular users are redirected to:

    http://127.0.0.1:8000/products/

---

## Step 2: View Products

Regular users can view available products from:

    http://127.0.0.1:8000/products/

Only products with stock greater than 0 are shown.

---

## Step 3: Add Product to Cart

Users can click the Add to Cart button from the product listing page.

Add to cart URL format:

    http://127.0.0.1:8000/add-to-cart/<product_id>/

Example:

    http://127.0.0.1:8000/add-to-cart/1/

If the product is already in the user's cart, the quantity is increased instead of creating a duplicate cart row.

---

## Step 4: View My Cart

Users can view their cart from:

    http://127.0.0.1:8000/my-cart/

The cart page shows:

* Product image
* Product name
* Price
* Quantity
* Item total
* Grand total
* Quantity increase button
* Quantity decrease button
* Remove button

---

## Step 5: Update Cart Quantity

Users can increase cart item quantity from:

    http://127.0.0.1:8000/increase-cart/<item_id>/

Users can decrease cart item quantity from:

    http://127.0.0.1:8000/decrease-cart/<item_id>/

If quantity becomes 0, the item is removed from the cart.

---

## Step 6: Remove Item from Cart

Users can remove cart items from:

    http://127.0.0.1:8000/remove-from-cart/<item_id>/

Remove is handled using a POST request with CSRF protection.

---

## Step 7: Checkout

Users can checkout from:

    http://127.0.0.1:8000/checkout/

After successful checkout:

* Product stock is reduced.
* User cart is cleared.
* User is redirected to the product page.

---

# 🔗 Key UI Endpoints

| Page | URL |
| ---- | --- |
| Home Page | `http://127.0.0.1:8000/` |
| Sign Up | `http://127.0.0.1:8000/signup/` |
| Sign In | `http://127.0.0.1:8000/signin/` |
| Logout | `http://127.0.0.1:8000/logout/` |
| Django Admin Panel | `http://127.0.0.1:8000/admin/` |
| Admin Dashboard | `http://127.0.0.1:8000/admin-dashboard/` |
| Admin Product Management | `http://127.0.0.1:8000/admin-products/` |
| Add Product | `http://127.0.0.1:8000/admin-products/add/` |
| Edit Product | `http://127.0.0.1:8000/admin-products/edit/<product_id>/` |
| Delete Product | `http://127.0.0.1:8000/admin-products/delete/<product_id>/` |
| Product List | `http://127.0.0.1:8000/products/` |
| Add to Cart | `http://127.0.0.1:8000/add-to-cart/<product_id>/` |
| My Cart | `http://127.0.0.1:8000/my-cart/` |
| Increase Quantity | `http://127.0.0.1:8000/increase-cart/<item_id>/` |
| Decrease Quantity | `http://127.0.0.1:8000/decrease-cart/<item_id>/` |
| Remove from Cart | `http://127.0.0.1:8000/remove-from-cart/<item_id>/` |
| Checkout | `http://127.0.0.1:8000/checkout/` |

---

# 🔌 Key API Endpoints

The following DRF API endpoints are available for Postman testing.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/cart/items/` | Get all API cart items |
| POST | `/api/cart/items/` | Add a new API cart item |
| GET | `/api/cart/items/<id>/` | Get a single API cart item |
| PUT | `/api/cart/items/<id>/` | Fully update an API cart item |
| PATCH | `/api/cart/items/<id>/` | Partially update an API cart item |
| DELETE | `/api/cart/items/<id>/` | Delete an API cart item |

---

# 🧪 Postman API Testing

The API can be tested using Token Authentication.

## Create Token from Django Admin

Go to:

    http://127.0.0.1:8000/admin/

Then:

    Tokens
    Add Token
    Select user
    Save
    Copy token key

## Create Token from Django Shell

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

## Postman Header

Use this header in Postman:

    Authorization: Token YOUR_TOKEN_HERE

Example:

    Authorization: Token abc123yourtoken

For POST, PUT, and PATCH requests, also use:

    Content-Type: application/json

Example API URL:

    http://127.0.0.1:8000/api/cart/items/

---

# 📦 API Cart Item Data Format

Example JSON body for adding an item through the API:

{
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00"
}

---

# 🔁 API Testing Examples

## GET All Items

Method:

    GET

URL:

    http://127.0.0.1:8000/api/cart/items/

Expected response:

    []

---

## POST Create Item

Method:

    POST

URL:

    http://127.0.0.1:8000/api/cart/items/

Body:

{
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00"
}

Expected response:

{
  "id": 1,
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00",
  "created_at": "2026-..."
}

---

## GET Single Item

Method:

    GET

URL:

    http://127.0.0.1:8000/api/cart/items/1/

---

## PUT Full Update

Method:

    PUT

URL:

    http://127.0.0.1:8000/api/cart/items/1/

Body:

{
  "product_id": 101,
  "product_name": "Smart Watch Updated",
  "quantity": 3,
  "price": "2600.00"
}

---

## PATCH Partial Update

Method:

    PATCH

URL:

    http://127.0.0.1:8000/api/cart/items/1/

Body:

{
  "quantity": 5
}

---

## DELETE Item

Method:

    DELETE

URL:

    http://127.0.0.1:8000/api/cart/items/1/

Expected response:

    204 No Content

---

# 🛍️ Product Data Format

Product data contains:

* Name
* Description
* Image
* Price
* Stock
* Created Date

Example product:

Product Name: Smart Watch

Description: Waterproof smart watch with Bluetooth calling.

Image: product image file

Price: 2500.00

Stock: 10

---

# ⚠️ Error Handling

The system returns clean structured error messages for common issues such as:

* User not authenticated
* User account not approved
* Regular user trying to access admin pages
* Admin user trying to access regular user pages
* Duplicate product ID in API
* Invalid input data
* Missing cart item
* Missing product
* Out of stock product
* Wrong URL or missing trailing slash
* Wrong HTTP method
* Invalid JSON format

Example validation error response:

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

Example authentication error response:

{
  "success": false,
  "error": "Authentication Error.",
  "details": {
    "detail": "Authentication credentials were not provided."
  },
  "suggestion": "Please login or provide a valid authentication token."
}

Example wrong URL response:

{
  "success": false,
  "error": "URL Syntax Error or Missing Trailing Slash.",
  "details": "The path '/wrong-url/' does not match any valid endpoint.",
  "suggestion": "Please verify your endpoint path and make sure it ends with slash (/). Example: /api/cart/items/5/"
}

---

# 📁 Main Project Structure

TRAINING PROJECT PRACTICE/
│
├── accounts/
│   ├── admin.py
│   ├── forms.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── accounts/
│           ├── home.html
│           ├── signup.html
│           └── signin.html
│
├── agent_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── cart/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── exceptions.py
│   └── templates/
│       └── cart/
│           ├── admin_dashboard.html
│           ├── admin_product_list.html
│           ├── admin_product_add.html
│           ├── admin_product_edit.html
│           ├── product_list.html
│           ├── my_cart.html
│           └── checkout.html
│
├── media/
│   └── product_images/
│
├── db.sqlite3
├── manage.py
└── requirements.txt

---

# 🧱 Main Models

## Product

Stores products created by admin.

Fields:

* name
* description
* image
* price
* stock
* created_at

---

## UserCartItem

Stores regular user cart items.

Fields:

* user
* product
* quantity
* added_at

The same user cannot have duplicate cart rows for the same product. If the user adds the same product again, quantity is increased.

---

## CartItem

Stores API cart items for Postman and DRF testing.

Fields:

* product_id
* product_name
* quantity
* price
* created_at

---

# 🔄 Main Website Flow

## Signup Flow

User opens signup page:

    /signup/

Then:

    User submits form
    SignUpForm validates data
    User is created with is_active=False
    User waits for admin approval

---

## Signin Flow

User opens signin page:

    /signin/

Then:

    User enters username/email and password
    signin_view searches user
    Password is checked
    is_active is checked
    is_staff is checked
    Admin goes to admin dashboard
    Regular user goes to products page

---

## Admin Product Flow

    Admin login
    Admin dashboard
    Product management page
    Add product
    Edit product
    Delete product

---

## Regular User Cart Flow

    Regular user login
    Product list
    Add to cart
    My cart
    Increase or decrease quantity
    Remove item
    Checkout
    Stock reduced
    Cart cleared

---

## API Flow

    Postman Request
    Token Authentication
    /api/cart/items/
    agent_system/urls.py
    cart/urls.py
    DRF Router
    CartItemViewSet
    CartItemSerializer
    CartItem Model
    Database
    JSON Response

---

# 🎯 Project Purpose

This project was built as a beginner-level Django learning project to understand:

* Django project and app structure
* Django apps
* Django settings
* Django URL routing
* Django views
* Django templates
* Django models and database migrations
* Django admin panel customization
* Django authentication system
* User signup and signin flow
* Admin approval workflow
* Role-based access control
* Admin product management system
* Product image upload using media files
* Cart and checkout system
* Cart quantity update
* Stock management
* Django REST Framework API development
* DRF serializers
* DRF routers
* DRF ViewSets
* API authentication and permissions
* Token authentication
* Postman API testing
* Custom exception handling in DRF

---

# ✅ Current System Summary

Admin can:

* Sign in
* Access admin dashboard
* Approve new users
* Add products
* Edit products
* Delete products
* Manage product image, description, price, and stock

Regular user can:

* Sign up
* Wait for admin approval
* Sign in after approval
* View available products
* Add products to cart
* Update cart quantity
* View cart
* Remove cart items
* Checkout products

Postman API can:

* Create cart item
* View cart item list
* Retrieve single cart item
* Update cart item
* Partially update cart item
* Delete cart item

The system now works as a multi-user role-based Django application with separate admin, regular user, and API testing functionality.