# Task Manager

A simple task management web application built with Django.

## Features

- Create, view, update, and delete tasks
- Task fields: Title, Description, Status (To Do, In Progress, Done)
- Responsive web interface
- REST API for task operations
- PostgreSQL support (SQLite by default)

## Tech Stack

- **Backend:** Django + Django REST Framework
- **Frontend:** Django Templates (HTML/CSS)
- **Database:** PostgreSQL / SQLite

## Setup Instructions

### 1. Create Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3. Configure Database (Optional - PostgreSQL)

Create a PostgreSQL database and set environment variables:
```powershell
$env:DJANGO_DB_ENGINE = "postgres"
$env:POSTGRES_DB = "task_manager"
$env:POSTGRES_USER = "postgres"
$env:POSTGRES_PASSWORD = "your_password"
$env:POSTGRES_HOST = "localhost"
$env:POSTGRES_PORT = "5432"
```

*Skip this step to use SQLite (default)*

### 4. Run Migrations
```powershell
python Task_Management\manage.py migrate
```

### 5. Start Server
```powershell
python Task_Management\manage.py runserver
```

### 6. Access Application

- **Web Interface:** http://127.0.0.1:8000/home/
- **API Endpoint:** http://127.0.0.1:8000/api/tasks/

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create new task |
| GET | `/api/tasks/{id}/` | Get specific task |
| PUT/PATCH | `/api/tasks/{id}/` | Update task |
| DELETE | `/api/tasks/{id}/` | Delete task |

### Example API Request
```powershell
curl -Method POST http://127.0.0.1:8000/api/tasks/ `
  -ContentType "application/json" `
  -Body '{"title":"Buy groceries","description":"Milk, eggs, bread","status":"todo"}'
```

## Using SQLite

SQLite is configured by default. No additional setup required!

To explicitly use SQLite:
```powershell
$env:DJANGO_DB_ENGINE = "sqlite"
python Task_Management\manage.py migrate
python Task_Management\manage.py runserver
```
