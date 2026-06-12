# DecodeLabs Internship Project - FastAPI REST API

## Overview

This project is a REST API built using **FastAPI**.  
It demonstrates backend development concepts including:

- CRUD operations
- Database integration (SQLite + SQLAlchemy ORM)
- User authentication
- Password hashing (Argon2)
- JWT-based authorization
- Protected routes

---

## Features

### Core Features
- User registration
- User login
- Full CRUD operations (Create, Read, Update, Delete)
- Request validation using Pydantic
- SQLite database persistence

### Security Features
- Password hashing using **Argon2**
- JWT authentication
- Protected routes requiring valid token

### Developer Features
- Auto-generated Swagger UI documentation
- Modular project structure
- ORM-based database handling (SQLAlchemy)

---

## Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Argon2-cffi
- Python-JOSE (JWT)

---

## Project Structure

```text
project_1/
│
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── database.py
├── auth.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/omar2301433/DecodeLabs-Internship-Project-3
cd DecodeLabs-Internship-Project-3
```

2. Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the server using:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```


## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Author

Omar Ahmed
