# Order and Customer Management System

This project is a web-based application built with Django that allows you to manage orders and customers, as well as organize and visualize data through a dashboard. The application includes features such as REST APIs, token-based authentication, CRUD operations, and filters for easy data management.

## Features

- **Order and Customer Management**: Easily manage customer information and track their orders.
- **Dashboard**: A user-friendly dashboard to visualize and organize customer and order data.
- **REST API**: Provides a fully functional REST API to access and manipulate data.
- **Token Authentication**: Secured access with token-based authentication using Django REST Framework.
- **Django Filters**: Allows filtering through orders and customers based on custom criteria.
- **CRUD Operations**: Full CRUD (Create, Read, Update, Delete) functionality for customers and orders.
- **Login/Signup**: User registration and login functionality with token-based authentication.
- **Custom Decorators**: Custom decorators for handling specific tasks and permissions in the API.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: Token-based authentication (DRF)
- **Database**: SQLite (or any other database supported by Django)
- **Frontend**: Django templates (or other frontend frameworks)
- **Others**: Django Filters, Decorators, CRUD operations

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## Usage

- **API Endpoints**: You can access the API endpoints for managing customers and orders via `/api/`.
- **Authentication**: Use token-based authentication by providing a token in the Authorization header.

## API Documentation

The API includes endpoints for managing:

- **Customers**: Create, Read, Update, Delete customer records.
- **Orders**: Create, Read, Update, Delete orders for customers.
- **Filters**: Apply filters to search for customers and orders based on specific criteria.

## Contributing

Feel free to submit issues or pull requests. Any contributions are welcome!
