# Refact Product API

A full-stack product management application built with **React, Flask, PostgreSQL, Docker, and JWT authentication**.

The project demonstrates a production-style backend architecture with REST APIs, authentication, database integration, automated testing, containerization, and a React frontend.

## Features

* User registration and login
* JWT-based authentication
* Product CRUD operations
* PostgreSQL database
* Flask REST API
* React frontend
* Docker and Docker Compose
* CORS configuration
* Automated tests with Pytest
* Environment-based configuration
* Git/GitHub version control

## Architecture

```text
React Frontend
      │
      │ HTTP / JSON
      ▼
Flask REST API
      │
      │ Psycopg
      ▼
PostgreSQL
```

The application can be run locally using Docker Compose:

```text
React → Flask API → PostgreSQL
```

## Technology Stack

### Backend

* Python 3.13
* Flask
* PostgreSQL 17
* Psycopg
* PyJWT
* Flask-CORS
* Gunicorn

### Frontend

* React
* Vite
* JavaScript
* React Router

### Testing & DevOps

* Pytest
* Docker
* Docker Compose
* Git
* GitHub

## Running the Project Locally

### Requirements

Install:

* Docker Desktop
* Git
* Node.js

### 1. Clone the repository

```bash
git clone git@github.com:DAVRUNKS/refact-product.git
cd refact-product
```

### 2. Start the backend

```bash
cd backend
docker compose up -d
```

Check the containers:

```bash
docker compose ps
```

The backend API will be available at:

```text
http://localhost:5000
```

### 3. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The React application will be available at:

```text
http://localhost:5173
```

## API Endpoints

### Public Endpoints

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| GET    | `/`              | API health check    |
| GET    | `/products`      | Get all products    |
| GET    | `/products/<id>` | Get one product     |
| POST   | `/register`      | Register a user     |
| POST   | `/login`         | Authenticate a user |

### Protected Endpoints

The following endpoints require a valid JWT:

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| POST   | `/products`      | Create a product |
| PUT    | `/products/<id>` | Update a product |
| DELETE | `/products/<id>` | Delete a product |

## Authentication

Authentication uses **JSON Web Tokens (JWT)**.

After logging in successfully, the API returns a token.

Protected requests use:

```text
Authorization: Bearer YOUR_JWT_TOKEN
```

The backend validates the token before allowing access to protected resources.

> Never commit JWT secrets, passwords, or other credentials to Git.

## Example API Requests

### Register a User

```http
POST /register
Content-Type: application/json
```

```json
{
  "username": "testuser",
  "password": "password123"
}
```

The password is securely hashed before being stored in PostgreSQL.

### Login

```http
POST /login
Content-Type: application/json
```

```json
{
  "username": "testuser",
  "password": "password123"
}
```

The successful response contains a JWT that can be used for protected requests.

### Create a Product

```http
POST /products
Authorization: Bearer YOUR_JWT_TOKEN
Content-Type: application/json
```

```json
{
  "name": "Laptop",
  "price": 500
}
```

Example response:

```json
{
  "message": "Product added successfully",
  "id": 1,
  "name": "Laptop",
  "price": 500.0
}
```

## Database

The application uses **PostgreSQL 17**.

When running through Docker Compose:

```text
PostgreSQL container
      │
      └── products_db
```

The database connection is configured using environment variables rather than hard-coded credentials.

The `.env` file is excluded from Git.

## Testing

The backend contains automated tests using Pytest.

Run the test suite inside the backend environment:

```bash
pytest
```

Current test result:

```text
19 passed
```

The tests cover authentication, product services, API routes, and validation.

## Docker

The backend is containerized using Docker.

Start the complete backend stack:

```bash
docker compose up -d
```

Stop it:

```bash
docker compose down
```

View running containers:

```bash
docker compose ps
```

View API logs:

```bash
docker compose logs api
```

View PostgreSQL logs:

```bash
docker compose logs db
```

## Environment Variables

The backend uses environment variables for configuration.

Example:

```env
POSTGRES_DB=products_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password

DB_HOST=db
DB_PORT=5432
DB_NAME=products_db
DB_USER=postgres
DB_PASSWORD=your_password

JWT_SECRET=your_secret

CORS_ORIGINS=http://localhost:5173
```

Do not commit the real `.env` file.

## Project Structure

```text
refact-product/
│
├── backend/
│   ├── app/
│   │   ├── database/
│   │   ├── routes/
│   │   ├── services/
│   │   └── ...
│   │
│   ├── tests/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── run.py
│
└── frontend/
    ├── src/
    ├── public/
    ├── package.json
    └── vite.config.js
```

## Development Workflow

The project follows a typical backend development workflow:

```text
Write Code
    ↓
Run Tests
    ↓
Run Docker Containers
    ↓
Test API
    ↓
Test React Frontend
    ↓
Commit Changes
    ↓
Push to GitHub
```

## Future Improvements

Potential future improvements include:

* API documentation with Swagger/OpenAPI
* Refresh tokens
* Role-based authorization
* Pagination
* Product search and filtering
* Database migrations
* CI/CD with GitHub Actions
* Production deployment
* Automated frontend tests
* Improved error handling and logging

## Author

**DAVRUNKS**

Built as a backend/full-stack portfolio project to demonstrate practical software engineering skills.

