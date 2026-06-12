# DecodeLabs Project 1 - FastAPI REST API

## Overview

This project is a simple REST API built using FastAPI. It demonstrates the implementation of basic API endpoints, request validation using Pydantic, and proper HTTP methods.

## Features

* Home endpoint
* Get all products
* Create a new product
* Request validation with Pydantic
* Interactive API documentation with Swagger UI

## Technologies Used

* Python 3.x
* FastAPI
* Uvicorn
* Pydantic

## Project Structure

```text
project1-api/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd project1-api
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

## API Endpoints

### GET /

Returns a welcome message.

Response:

```json
{
  "message": "Welcome to DecodeLabs Project 1 API"
}
```

### GET /products

Returns a list of products.

Response:

```json
{
  "products": []
}
```

### POST /products

Creates a new product.

Request Body:

```json
{
  "name": "Laptop",
  "price": 999.99
}
```

Response:

```json
{
  "message": "Product created successfully",
  "product": {
    "name": "Laptop",
    "price": 999.99
  }
}
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Author

Omar Ahmed
