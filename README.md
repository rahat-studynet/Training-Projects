# Automated Cart Management System

A beginner-friendly full-stack Django and Django REST Framework (DRF) application for managing cart items with user registration, admin approval, authentication, and a dynamic frontend UI.

The system allows users to sign up, but new users cannot access the cart system until an admin verifies/approves them from the Django admin panel. After approval, users can sign in and use the cart features such as viewing, adding, and deleting cart items.

---

## 🚀 Features

### User Authentication & Approval

* **Home Page:** Includes Sign Up, Sign In, and Admin Panel options.
* **User Sign Up:** New users can register using username, email, password, and confirm password.
* **Validation System:** Checks duplicate username, duplicate email, password length, password match, and password strength.
* **Admin Approval System:** Newly registered users are saved as `Not Verified` by default.
* **Verified User Login:** Users can sign in only after admin approval.
* **Custom Admin Panel Status:** Admin can see user verification status as `Verified` or `Not Verified`.
* **Logout System:** Logged-in users can securely log out and return to the home page.

### Cart Management

* **Cart Dashboard View:** Displays cart items dynamically in an HTML table using JavaScript Fetch API.
* **Add Item Form:** Allows approved users to add new cart items through a frontend form.
* **Delete Item:** Allows users to delete cart items from the dashboard.
* **Dynamic API Integration:** Frontend pages communicate with DRF API endpoints asynchronously.
* **CSRF Protection:** POST and DELETE requests are protected using CSRF tokens.
* **Login Required UI Pages:** Cart pages are only accessible after user login.

### API & Exception Handling

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

---

#### 📋 Installation & Local Setup

## 1. Clone the Repository
git clone https://github.com/rahat-studynet/Training-Projects
cd "Training Projects"


## 2. Set Up a Virtual Environment
# Create the virtual environment
python -m venv .venv

# Activate the environment on Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Activate the environment on Mac/Linux
source .venv/bin/activate


## 3. Install Dependencies
pip install -r requirements.txt


## 4. Run Database Migrations
python manage.py migrate

## 5. Create a Superuser
Create an admin account to approve new users and manage the system.
python manage.py createsuperuser

## 6. Start the Development Server
python manage.py runserver

The application will be accessible locally at:
http://127.0.0.1:8000/
🔐 User Approval Workflow

# Step 1: User Sign Up

A new user goes to:
http://127.0.0.1:8000/signup/

The user enters:
Username
Email
Password
Confirm Password

After successful signup, the account is created as:

Not Verified

This means the user cannot sign in yet.

# Step 2: Admin Approval

Admin goes to:

http://127.0.0.1:8000/admin/

Then admin can approve the user from the user list by setting the account as active/verified.

After approval, the user status becomes:

Verified

# Step 3: User Sign In

Approved users can sign in from:

http://127.0.0.1:8000/signin/

After successful login, the user is redirected to the cart dashboard:

http://127.0.0.1:8000/api/cart/view/


### Key UI Endpoints

| Page               | URL                                    |
| ------------------ | -------------------------------------- |
| Home Page          | `http://127.0.0.1:8000/`               |
| Sign Up            | `http://127.0.0.1:8000/signup/`        |
| Sign In            | `http://127.0.0.1:8000/signin/`        |
| Logout             | `http://127.0.0.1:8000/logout/`        |
| Cart Dashboard     | `http://127.0.0.1:8000/api/cart/view/` |
| Add Cart Item      | `http://127.0.0.1:8000/api/cart/add/`  |
| Django Admin Panel | `http://127.0.0.1:8000/admin/`         |


### Key API Endpoints

| Method | Endpoint                | Description                  |
| ------ | ----------------------- | ---------------------------- |
| GET    | `/api/cart/items/`      | Get all cart items           |
| POST   | `/api/cart/items/`      | Add a new cart item          |
| GET    | `/api/cart/items/<id>/` | Get a single cart item       |
| PUT    | `/api/cart/items/<id>/` | Fully update a cart item     |
| PATCH  | `/api/cart/items/<id>/` | Partially update a cart item |
| DELETE | `/api/cart/items/<id>/` | Delete a cart item           |


### Postman API Testing

The API can be tested using Token Authentication.

Use this header in Postman:

Authorization: Token YOUR_TOKEN_HERE

Example:

Authorization: Token abc123yourtoken

Example API URL:

http://127.0.0.1:8000/api/cart/items/
📦 Cart Item Data Format

Example JSON body for adding an item:

{
  "product_id": 101,
  "product_name": "Smart Watch",
  "quantity": 2,
  "price": "2500.00"
}


### ⚠️ Error Handling

The system returns clean structured error messages for common issues such as:

User not authenticated
User account not approved
Duplicate product ID
Invalid input data
Missing cart item
Wrong URL or missing trailing slash
Wrong HTTP method
Invalid JSON format

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

#### Main Project Structure

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
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── exceptions.py
│   └── templates/
│       └── cart/
│           ├── cart_list.html
│           └── add_item.html
│
├── Navpage/
├── db.sqlite3
├── manage.py
└── requirements.txt

## Project Purpose

This project was built as a beginner-level Django learning project to understand:

Django project and app structure
Django models and database migrations
Django admin panel customization
Django authentication system
User signup and signin flow
Admin approval workflow
Django REST Framework API development
API authentication and permissions
Frontend-to-backend communication using Fetch API
Custom exception handling in DRF