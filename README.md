# Task Manager
A simple Task Management web application built with Django.

## Features (core requirements)
- Create, view, update, and delete tasks
- Task fields: Title, Description, Status (To Do / In Progress / Done)
- Responsive web interface
- REST API for task operations
- Persistent storage supports PostgreSQL (SQLite default for quick local dev)

## Tech stack
- Backend: Django + Django REST Framework
- Frontend: Django templates (HTML/CSS)
- Database: PostgreSQL / SQLite

## Local setup (Windows / PowerShell)
### 1) Create & activate a virtual environment
```powershell path=null start=null
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies
```powershell path=null start=null
pip install -r requirements.txt
```

### 3) Run migrations
```powershell path=null start=null
python manage.py migrate
```

### 4) Start the server
```powershell path=null start=null
python manage.py runserver
```

Then open:
- UI: `http://127.0.0.1:8000/home/`
- API: `http://127.0.0.1:8000/api/tasks/`

## Enable PostgreSQL (optional locally, required for production)
```powershell path=null start=null
$env:DJANGO_DB_ENGINE = "postgres"
$env:POSTGRES_DB = "task_manager"
$env:POSTGRES_USER = "postgres"
$env:POSTGRES_PASSWORD = "your_password"
$env:POSTGRES_HOST = "localhost"
$env:POSTGRES_PORT = "5432"
```

## REST API (Task CRUD)
Base URL: `/api/tasks/`
- `GET /api/tasks/` list tasks
- `POST /api/tasks/` create task
- `GET /api/tasks/{id}/` retrieve task
- `PUT/PATCH /api/tasks/{id}/` update task
- `DELETE /api/tasks/{id}/` delete task

Example create:
```powershell path=null start=null
curl -Method POST http://127.0.0.1:8000/api/tasks/ `
  -ContentType "application/json" `
  -Body '{"title":"Buy groceries","description":"Milk, eggs, bread","status":"todo"}'
```

## Deploy to Render (recommended)
### Render settings
- Build Command:
  - `bash build.sh`
- Start Command:
  - `python -m gunicorn Task_Management.wsgi:application --bind 0.0.0.0:$PORT`

### Render environment variables
- `DJANGO_SECRET_KEY` = a long random secret
- `DJANGO_DEBUG` = `False`
- `DJANGO_ALLOWED_HOSTS` = `your-service-name.onrender.com`

Database env vars:
- `DJANGO_DB_ENGINE` = `postgres`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

### First deploy migration
After the first deploy, open Render Shell and run:
- `python manage.py migrate`
