# E-Commerce Backend (ALX)
## Overview

This project is a production-ready e-commerce backend built with Django and Django REST Framework.
It simulates a real-world backend system focused on scalability, security, performance, and clean API design.

The backend provides:

Secure user authentication (JWT)

CRUD APIs for products and categories

Filtering, sorting, and pagination

Optimized PostgreSQL database schema

Public API documentation via Swagger/OpenAPI

## Project Objectives

Design and optimize a relational database schema

Build RESTful APIs for frontend integration

Implement efficient querying with filtering and indexing

Provide clear, testable API documentation

Follow ALX backend engineering standards

## Technologies Used
Technology	Purpose
Python	Core programming language
Django	Backend framework
Django REST Framework	API development
PostgreSQL	Relational database
JWT (SimpleJWT)	Secure authentication
Swagger / OpenAPI	API documentation
🏗️ System Architecture
flowchart LR
    Client -->|HTTP / JSON| DjangoAPI[Django REST API]
    DjangoAPI --> Auth[JWT Authentication]
    DjangoAPI --> DB[(PostgreSQL)]
    DjangoAPI --> Docs[Swagger UI]

## Database Schema (Overview)
erDiagram
    CATEGORY ||--o{ PRODUCT : contains
    CATEGORY {
        int id
        string name
    }
    PRODUCT {
        int id
        string name
        text description
        decimal price
        datetime created_at
    }


Optimizations

Indexed fields: Product.name, Product.price

Foreign key relationships for efficient joins

## Key Features
1. Authentication

JWT-based login and registration

Stateless and secure

2. CRUD Operations

Products

Categories

3. Product Discovery

Filtering by category

Sorting by price

Pagination for large datasets

4. API Documentation

Interactive Swagger UI

Publicly accessible

## API Endpoints (Examples)
Authentication
POST /api/auth/register/
POST /api/auth/token/

Products
GET    /api/products/
POST   /api/products/
GET    /api/products/{id}/
PUT    /api/products/{id}/
DELETE /api/products/{id}/

Filtering & Sorting
GET /api/products/?category=Electronics
GET /api/products/?ordering=price
GET /api/products/?ordering=-price

#API Documentation

Swagger UI is available at:

/swagger/


Example:

http://localhost:8000/swagger/

## Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd alx-ecommerce-backend

2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment Variables
SECRET_KEY=your-secret-key
DB_NAME=ecommerce
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Start the Server
python manage.py runserver

## Testing

Run all tests:

python manage.py test


Tests cover:

Models and constraints

CRUD APIs

Filtering and sorting

Authentication

Swagger accessibility

## Performance Considerations

Database indexing for frequent queries

Pagination to limit payload size

Optimized queryset filtering

## Deployment Notes

Set DEBUG=False in production

Use PostgreSQL in production

Configure environment variables on the hosting platform

Ensure /swagger/ remains publicly accessible

## Key Takeaways

Clean API design improves frontend integration

Database indexing significantly boosts performance

JWT enables scalable authentication

Swagger is essential for developer experience

Testing prevents common production failures
