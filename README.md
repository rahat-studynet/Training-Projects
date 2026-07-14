# Automated Product & Cart Management System

A beginner-friendly full-stack Django and Django REST Framework (DRF) application with role-based access for admin users and regular users.

The system allows users to sign up, but newly registered users cannot access the system until an admin verifies/approves them from the Django admin panel. After approval, users can sign in. Admin users can manage products through a simple content management system, while regular users can view products, add them to cart, remove cart items, and complete checkout.

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
| Regular User | Can view products, add products to cart, remove cart items, and checkout |
| Not Verified User | Cannot sign in until approved by admin |

---

## Admin Product Management System

Admin users can manage products from a custom CMS page.

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
* **Stock Checking:** Users cannot add more quantity than available stock.
* **My Cart Page:** Shows cart items, quantity, item total, and grand total.
* **Remove Item:** Users can remove items from their cart.
* **Checkout:** Users can confirm checkout.
* **Stock Reduction:** Product stock is reduced after successful checkout.
* **Cart Clear After Checkout:** User cart becomes empty after checkout.

---

## Legacy Cart API System

The previous DRF cart API system is still available.

### API Features

* **DRF ModelViewSet:** Provides list, create, retrieve, update, partial update, and delete operations.
* **Token Authentication:** API requests can be tested using DRF token authentication.
* **Session Authentication:** Browser-based login works using Django session authentication.
* **Custom Exception Handler:** Returns clean error responses for authentication errors, validation errors, missing items, invalid URLs, wrong HTTP methods, and bad JSON.
* **URL Fallback Handler:** Invalid or missing-slash URLs return a structured error response.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Authentication:** Django Authentication System, DRF Token Authentication, Session Authentication
* **Admin Panel:** Django Admin
* **Image Upload:** Pillow, Django Media Files

---

# 📋 Installation & Local Setup

## 1. Clone the Repository

git clone https://github.com/rahat-studynet/Training-Projects
cd "Training Projects"

---

## 2. Set Up a Virtual Environment

python -m venv .venv

### Activate the environment on Windows PowerShell

.\.venv\Scripts\Activate.ps1

### Activate the environment on Mac/Linux

source .venv/bin/activate

---

## 3. Install Dependencies

pip install -r requirements.txt

If Pillow is not already installed, install it manually:

pip install Pillow

---

## 4. Run Database Migrations

python manage.py makemigrations
python manage.py migrate

If only cart app changes are needed:

python manage.py makemigrations cart
python manage.py migrate

---

## 5. Create a Superuser

Create an admin account to approve users and manage products.

python manage.py createsuperuser

---

## 6. Start the Development Server

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

Then admin can approve the user from the user list by setting the account as active/verified.

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

## Step 2: Manage Products

Admin can manage products from:

http://127.0.0.1:8000/admin-products/

Admin can:

* View product list
* Add new product
* Edit product
* Delete product

---

## Step 3: Add Product

Admin can add products from:

http://127.0.0.1:8000/admin-products/add/

Product fields:

* Product Name
* Description
* Product Image
* Price
* Stock

---

## Step 4: Edit Product

Admin can edit a product from:

http://127.0.0.1:8000/admin-products/edit/<product_id>/

---

## Step 5: Delete Product

Admin can delete a product from:

http://127.0.0.1:8000/admin-products/delete/<product_id>/

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

If the product is already in the user's cart, the quantity is increased.

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
* Remove button

---

## Step 5: Remove Item from Cart

Users can remove cart items from:

http://127.0.0.1:8000/remove-from-cart/<item_id>/

---

## Step 6: Checkout

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
| Remove from Cart | `http://127.0.0.1:8000/remove-from-cart/<item_id>/` |
| Checkout | `http://127.0.0.1:8000/checkout/` |
| Legacy Cart Dashboard | `http://127.0.0.1:8000/api/cart/view/` |
| Legacy Add Cart Item | `http://127.0.0.1:8000/api/cart/add/` |

---

# 🔌 Key API Endpoints

The following DRF API endpoints are available for the legacy cart system.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/cart/items/` | Get all legacy cart items |
| POST | `/api/cart/items/` | Add a new legacy cart item |
| GET | `/api/cart/items/<id>/` | Get a single legacy cart item |
| PUT | `/api/cart/items/<id>/` | Fully update a legacy cart item |
| PATCH | `/api/cart/items/<id>/` | Partially update a legacy cart item |
| DELETE | `/api/cart/items/<id>/` | Delete a legacy cart item |

---

# 🧪 Postman API Testing

The API can be tested using Token Authentication.

Use this header in Postman:

Authorization: Token YOUR_TOKEN_HERE

Example:

Authorization: Token abc123yourtoken

Example API URL:

http://127.0.0.1:8000/api/cart/items/

---

# 📦 Legacy Cart Item Data Format

Example JSON body for adding an item through the API:

{
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00"
}

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
Description: Waterproof smart watch
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
* Duplicate product ID in legacy API
* Invalid input data
* Missing cart item
* Missing product
* Out of stock product
* Wrong URL or missing trailing slash
* Wrong HTTP method
* Invalid JSON format

Example error response:

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

# 📁 Main Project Structure

TRAINING PROJECTS/
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
│           ├── checkout.html
│           ├── cart_list.html
│           └── add_item.html
│
├── Navpage/
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

Stores legacy API cart items.

Fields:

* product_id
* product_name
* quantity
* price
* created_at

---

# 🎯 Project Purpose

This project was built as a beginner-level Django learning project to understand:

* Django project and app structure
* Django models and database migrations
* Django admin panel customization
* Django authentication system
* User signup and signin flow
* Admin approval workflow
* Role-based access control
* Admin content management system
* Product image upload using media files
* Cart and checkout system
* Stock management
* Django REST Framework API development
* API authentication and permissions
* Frontend-to-backend communication using Fetch API
* Custom exception handling in DRF

---

# ✅ Current System Summary

Admin can:

* Sign in after approval
* Access admin dashboard
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
* View cart
* Remove cart items
* Checkout products

The system now works as a multi-user role-based Django application with separate admin and regular user functionality.