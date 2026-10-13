# DRF Project

This project is a Django REST Framework (DRF) application for building and testing REST APIs with authentication, CRUD operations, and Swagger documentation.

It includes multiple API modules, JWT authentication, user registration/login, and CRUD endpoints for employee data.

## Features

- Django 5.x backend with DRF
- JWT authentication using `djangorestframework-simplejwt`
- User registration and login APIs
- CRUD APIs for employee records
- Versioned API structure (`v1` and `v2`)
- Swagger UI and Redoc documentation
- SQLite database for local development
- CORS and throttling support

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- JWT
- Swagger / OpenAPI
- django-cors-headers

## Project Structure

```text
S1_Drf/
├── README.md
├── drfProject/
│   ├── account/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializer.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── crud/
│   │   ├── migrations/
│   │   ├── v1/
│   │   ├── v2/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   └── ...
│   ├── drfApp/
│   │   ├── migrations/
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   ├── drfProject/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── db.sqlite3
└── ...
```

## Prerequisites

- Python 3.10 or higher
- pip
- virtual environment recommended

## Installation

1. Open a terminal in the project folder:

```bash
cd drfProject
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install django djangorestframework django-filter djangorestframework-simplejwt drf-yasg django-cors-headers
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional for admin access):

```bash
python manage.py createsuperuser
```

## Run the Project

```bash
python manage.py runserver
```

Then open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

## API Endpoints

### General app

- `GET /api/test`
- `GET /api/test/<id>`

### Authentication

- `POST /api/token/` - obtain JWT token
- `POST /api/token/refresh/` - refresh JWT token

### Account APIs

- `GET /account/`
- `POST /account/register/`
- `POST /account/login/`

### CRUD API v1

- `GET /api/v1/view/`
- `POST /api/v1/view/`
- `GET /api/v1/view/<id>/`
- `PUT /api/v1/view/<id>/`
- `PATCH /api/v1/view/<id>/`
- `DELETE /api/v1/view/<id>/`

### CRUD API v2

- `GET /api/v2/view/`
- `POST /api/v2/view/`
- `GET /api/v2/view/<id>/`
- `PUT /api/v2/view/<id>/`
- `PATCH /api/v2/view/<id>/`
- `DELETE /api/v2/view/<id>/`

## API Documentation

Swagger documentation is available at:

- http://127.0.0.1:8000/swagger/v1/
- http://127.0.0.1:8000/swagger/v2/
- http://127.0.0.1:8000/redoc/

## Notes

- The app uses SQLite by default for development.
- The project includes rate limiting and basic authentication configuration in the DRF settings.
- For production, update the `SECRET_KEY`, enable secure settings, configure a production database, and set allowed hosts properly.

## License

This project is for learning and development purposes unless you specify otherwise.
