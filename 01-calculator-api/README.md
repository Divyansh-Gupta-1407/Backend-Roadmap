# Calculator API

Welcome to **Project 01** of the backend learning journey! This project is a lightweight, production-ready **Calculator API** built with **FastAPI** and **Uvicorn**.

The goal of this project is to move beyond writing local Python scripts and start building web-accessible HTTP APIs.

---

## Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- ✅ Automatic request validation
- ✅ JSON responses
- ✅ Proper HTTP error handling
- ✅ Interactive Swagger API documentation

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn

---

## Core Concepts Learned

This project focuses on the fundamentals of backend API development:

- Creating a FastAPI application
- Building API endpoints using routing decorators (`@app.get`)
- Running an ASGI server with Uvicorn
- Using query parameters
- Python type hints for automatic validation
- Returning structured JSON responses
- Raising `HTTPException` for invalid operations
- Handling edge cases such as division by zero

---

## Request Lifecycle

When a client sends a request like:

```text
/divide?a=10&b=2
```

The request flows through the following stages:

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
   [ Parameter Validation ]
    (float type conversion)
                │
                ▼
       [ Your Endpoint ]
     (divide_numbers())
                │
                ▼
      [ Business Logic ]
    (division + error check)
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
calculator-api/
│── main.py
│── requirements.txt
└── README.md
```

---

## Code

```python
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Calculator API")

@app.get("/add")
def add_numbers(a: float, b: float) -> dict[str, float]:
    return {"result": a + b}

@app.get("/subtract")
def subtract_numbers(a: float, b: float) -> dict[str, float]:
    return {"result": a - b}

@app.get("/multiply")
def multiply_numbers(a: float, b: float) -> dict[str, float]:
    return {"result": a * b}

@app.get("/divide")
def divide_numbers(a: float, b: float) -> dict[str, float]:
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )
    return {"result": a / b}
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

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/add` | Adds two numbers |
| GET | `/subtract` | Subtracts two numbers |
| GET | `/multiply` | Multiplies two numbers |
| GET | `/divide` | Divides two numbers |

---

## 🧪 Example Requests

### Addition

```http
GET /add?a=10&b=20
```

Response

```json
{
    "result": 30.0
}
```

---

### Subtraction

```http
GET /subtract?a=20&b=5
```

Response

```json
{
    "result": 15.0
}
```

---

### Multiplication

```http
GET /multiply?a=6&b=7
```

Response

```json
{
    "result": 42.0
}
```

---

### Division

```http
GET /divide?a=20&b=4
```

Response

```json
{
    "result": 5.0
}
```

---

### Division by Zero

```http
GET /divide?a=10&b=0
```

Status Code

```text
400 Bad Request
```

Response

```json
{
    "detail": "Cannot divide by zero"
}
```

---

## Interactive API Documentation

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

- Building REST APIs with FastAPI
- Working with query parameters
- Using Python type hints for validation
- Returning JSON responses
- Raising HTTP exceptions
- Running an ASGI server using Uvicorn
- Understanding the request-response lifecycle
- Creating interactive API documentation


---

## Author
**Divyansh Gupta**


