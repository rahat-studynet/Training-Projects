# Automated Cart Management System

A simple, robust full-stack Django and Django REST Framework (DRF) application that manages cart items. The project features a dual-screen dynamic frontend UI that interacts asynchronously with a secure, validated database backend.

## 🚀 Features

* **Screen 1 (Dashboard View):** A dynamic HTML table that securely fetches and renders database cart items asynchronously using vanilla JavaScript. Includes real-time item deletion capabilities.
* **Screen 2 (Add Item Form):** A clean user input form with client-side parsing and structured JSON payloads to add items to the cart.
* **Layer 2 Exception Interception:** Custom backend validation that catches database integrity errors (e.g., duplicate product entries) and returns clean, human-readable feedback.
* **API Security:** Endpoints protected via Django REST Framework's `SessionAuthentication` and `IsAuthenticated` policies to ensure only verified administrators modify data.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django 6.0.6, Django REST Framework 3.17.1
* **Database:** SQLite3
* **Frontend:** Vanilla JavaScript (Fetch API), HTML5, CSS3

---

## 📋 Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd "Training Projects"
```

### 2. Set Up a Virtual Environment
```bash
# Create the virtual environment
python -m venv .venv

# Activate the environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate the environment (Mac/Linux)
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)
To interact with the authenticated API endpoints, create an administrator account:
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```
The application will be accessible locally at `http://127.0.0.1:8000/`.

---

## 🔗 Key API & UI Endpoints

* **Dashboard View (UI):** `http://127.0.0.1:8000/api/cart/view/`
* **Add Item Form (UI):** `http://127.0.0.1:8000/api/cart/add/`
* **Django Admin Panel:** `http://127.0.0.1:8000/admin/`