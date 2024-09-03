# BookStore

BookStore is a comprehensive web application for an online bookstore, serving as both a consolidation of my current web development knowledge and a platform for exploring new technologies and practices. This project represents a culmination of my skills while also pushing the boundaries of my expertise into new areas.


## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [API Documentation](#api-documentation)

## Features

- Extensive book catalog with search and filter functionality
- User registration and authentication system
- Shopping cart and order management
- *in progres...*

## Technologies

- Backend: Python 3.12, Django 5.0, Django REST Framework 3.15
- Frontend: Next.js 14.2, React 18
- Database: PostgreSQL 16.0
- Authentication: SimpleJWT 5.3
- Testing: pytest-django 4.8
- Server: Nginx 1.27, Gunicorn 22.0
- Containerization: Docker, Docker Compose
- *in progres...*

## Getting Started

### Prerequisites

- Docker and Docker Compose
- *in progres...*

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/dejvinczi/bookstore.git
   cd bookstore
   ```
2. Create .env file from .env.template:
   ```
   cp .env.template .env
   ```

3. Build and run the Docker containers:
   ```
   # development
   docker-compose -f development.yml build 

   # production
   docker-compose -f production.yml build
   ```

## Usage

1. Navigate to the root directory of the repository:
   ```
   cd bookstore
   ```

2. Run docker containers:
   ```
   # development
   docker-compose -f development.yml up 

   # production
   docker-compose -f production.yml up
   ```

## Testing

You can run tests with coverage using `pytest` on the development server:


1. Navigate to the root directory of the repository:
   ```
   cd bookstore
   ```

2. Run docker development composition:
   ```
   docker-compose -f development.yml up 
   ```

3. In another terminal attach to the development api server console:
   ```
   docker-compose -f exec -it bookstore-dev-api-1 bash
   ```

4. Run tests:
   ```
   pytest
   ```

## API Documentation

API documentation is available when the development server is running at:
1. Swagger:  `http://localhost:8000/api/schema/swagger-ui/` 
2. Redoc:  `http://localhost:8000/api/schema/redoc/`
3. JSON:  `http://localhost:8000/api/schema/`