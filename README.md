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
- Sending order confirmation emails to users
- *in progres...*

## Technologies

- Backend: Python v3.12, Django v5.0, Django REST Framework v3.15
- Frontend: Next.js v14.2, React v18
- Database: PostgreSQL v16.0
- Authentication: SimpleJWT v5.3
- Testing: pytest-django v4.8
- Server: Gunicorn v22.0
- Proxy: Nginx v1.27
- Containerization: Docker v27.2, Docker Compose v2.22
- Distributed Task Queue: Celery v5.4.0
- Message Broker: Redis v7.4
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
2. Create .env file from .env.template and edit it:
   ```
   cp .env.template .env
   ```

3. Build the Docker containers (choose one of the following as appropriate):
   
   3.1. Development composition:
   ```
   docker-compose -f development.yml build
   ```
   3.2. Testing composition:
   ```
   docker-compose -f testing.yml build
   ```
   3.3. Production composition:
   ```
   docker-compose -f production.yml build
   ```

## Usage

1. Navigate to the root directory of the repository:
   ```
   cd bookstore
   ```

3. Run the Docker containers (choose one of the following as appropriate):
   
   3.1. Development composition:
   ```
   docker-compose -f development.yml up
   ```
   3.2. Testing composition:
   ```
   docker-compose -f testing.yml up
   ```
   3.3. Production composition:
   ```
   docker-compose -f production.yml up
   ```

## Testing

You can run tests with coverage using `pytest` on the testing server:


1. Navigate to the root directory of the repository:
   ```
   cd bookstore
   ```

2. Run docker testing composition:
   ```
   docker-compose -f testing.yml up 
   ```

3. In another terminal attach to the development api server console:
   ```
   docker-compose -f exec -it bookstore-test-api-1 bash
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