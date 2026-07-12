# Todo API

Welcome to **Project 02** of the backend learning journey! This project is a lightweight **Todo API** built with **FastAPI** and **Uvicorn**.

Unlike the Calculator API, this project introduces **stateful APIs**, allowing clients to create, retrieve, update, and delete todo items using REST principles.

---

## Features

- ✅ Create a new todo
- 📋 Retrieve all todos
- 🔍 Retrieve a todo by ID
- ✏️ Partially update a todo
- 🗑️ Delete a todo
- ✅ Automatic request validation
- ✅ UUID-based identifiers
- ✅ Structured JSON responses
- ✅ Proper HTTP status codes and error handling
- ✅ Interactive Swagger API documentation

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## Core Concepts Learned

This project expands upon the fundamentals of API development by introducing:

- CRUD operations (Create, Read, Update, Delete)
- Request bodies
- Path parameters
- UUIDs for unique identifiers
- Pydantic models for validation
- Multiple request and response models
- Response models
- RESTful API design
- HTTP exceptions
- Business rule validation
- In-memory data storage
- Partial updates using `PATCH`
- Proper HTTP status codes

---

## Request Lifecycle

When a client sends a request like:

```text
PATCH /todos/{id}
```

The request follows this flow:

```text
       [ Browser / Client ]
                │
      HTTP Request
                │
                ▼
          [ Uvicorn ]
      (ASGI Web Server)
                │
                ▼
          [ FastAPI ]
       (Routing Engine)
                │
                ▼
    [ Path & Body Validation ]
      (UUID + Pydantic Model)
                │
                ▼
       [ Your Endpoint ]
         (patch_todo())
                │
                ▼
      [ Business Logic ]
    (Find → Update → Save)
                │
                ▼
    [ JSON Serialization ]
                │
                ▼
        HTTP JSON Response
```

---

## Project Structure

```text
todo-api/
│── main.py
│── requirements.txt
└── README.md
```

---

## Installation

Install the required dependencies:

```bash
pip install fastapi uvicorn
```

---

## Run the Server

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/todos` | Create a new todo |
| GET | `/todos` | Retrieve all todos |
| GET | `/todos/{id}` | Retrieve a todo by ID |
| PATCH | `/todos/{id}` | Partially update a todo |
| DELETE | `/todos/{id}` | Delete a todo |

---

## Example Requests

### Create Todo

```http
POST /todos
```

Request Body

```json
{
    "title": "Learn FastAPI",
    "completed": false
}
```

Response

```json
{
    "id": "2b2ef0e3-5d6b-4f2f-a52d-f85c8d6e6d1f",
    "title": "Learn FastAPI",
    "completed": false
}
```

---

### Get All Todos

```http
GET /todos
```

Response

```json
[
    {
        "id": "...",
        "title": "Learn FastAPI",
        "completed": false
    }
]
```

---

### Get Todo by ID

```http
GET /todos/{id}
```

Response

```json
{
    "id": "...",
    "title": "Learn FastAPI",
    "completed": false
}
```

---

### Update Todo

```http
PATCH /todos/{id}
```

Request Body

```json
{
    "completed": true
}
```

Response

```json
{
    "id": "...",
    "title": "Learn FastAPI",
    "completed": true
}
```

---

### Delete Todo

```http
DELETE /todos/{id}
```

Response

```json
{
    "message": "Todo deleted successfully."
}
```

---

## Endpoint Responsibilities

```text
create_todo
└── Creates a new todo and returns the newly created resource.

get_all_todos
└── Returns every todo stored in memory.

get_by_id
└── Retrieves a single todo using its UUID.

patch_todo
└── Applies partial updates and returns the updated todo.

delete_todo
└── Removes a todo and returns a confirmation message.
```

---

## 📖 Interactive API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## What I Learned

By completing this project, I learned how to build a fully functional REST API using FastAPI.

Key concepts include:

- CRUD operations
- Request bodies
- Path parameters
- UUIDs
- Pydantic models
- Multiple data models
- Response models
- HTTP exceptions
- REST API design
- Business rule validation
- In-memory storage
- Partial updates (`PATCH`)
- Proper HTTP status codes
- Building stateful web APIs
--- 

## Author
**Divyansh Gupta**
