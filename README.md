# userAppBackendUsingDjango
User Management API with Django & JWT Authentication
📌 Project Overview
This is a Django REST API for user management, featuring JWT authentication, PostgreSQL integration, and role-based permissions. The API allows users to register, log in, update their profiles, and manage authentication tokens securely.

🚀 Features
✅ User Registration & Authentication (JWT-based)
✅ CRUD Operations on User Data
✅ Role-Based Access Control (RBAC)
✅ Custom Permissions for API security
✅ Hashed Password Storage for enhanced security
✅ PostgreSQL Database Integration
✅ Deployed on Render

🔧 Technologies Used
Django (Backend Framework)

Django REST Framework (DRF) (API Development)

Simple JWT (Authentication)

PostgreSQL (Database)

Render (Deployment)



🔑 Authentication & Usage
1️⃣ Register a new user:

POST /api/users/
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword"
}


2️⃣ Obtain JWT token:

POST /api/token/
{
  "username": "testuser",
  "password": "securepassword"
}


3️⃣ Access Protected Endpoints (Include JWT in headers):

Authorization: Bearer <your_access_token>


🚀 Deployment on Render
PostgreSQL database configured with dj-database-url

Environment variable DATABASE_URL set in Render


📌 How to Run Locally
1️⃣ Clone the Repository


git clone https://github.com/Divyansh031/userAppBackendUsingDjango.git
cd userAppBackendUsingDjango


2️⃣ Create a Virtual Environment


python -m venv env
source env/bin/activate  # (For Windows: env\Scripts\activate)


3️⃣ Install Dependencies


pip install -r requirements.txt


4️⃣ Run Migrations

python manage.py makemigrations
python manage.py migrate


5️⃣ Start the Server


python manage.py runserver



