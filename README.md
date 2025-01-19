# Cafe Management System

This is a web-based cafe management system built with **Django**, **Python**, and **HTML/CSS**. The application allows users to manage orders, dishes, and tables in a cafe environment. It includes features for viewing, adding, editing, and deleting orders, as well as managing dishes and table status.

## Features

- **Manage Orders**: View, add, update, and delete orders.
- **Manage Dishes**: View and edit the cafe's menu.
- **Manage Tables**: View and edit the status of tables (e.g., number of seats).
- **Responsive Design**: User interface is responsive and optimized for different screen sizes.
- **REST API**: Exposes endpoints for managing orders, dishes, and tables.

## Tech Stack

- **Backend**: Django, Django Rest Framework (DRF)
- **Frontend**: HTML, CSS, TailwindCSS
- **Database**: PostgreSQL
- **API**: RESTful API for managing orders, dishes, and tables
- **Version**: Python 3.8+, Django 4+
- **Docker**: Docker version 27.4.0
- **Nginx**: nginx:1.23-alpine
- **Gunicorn**:

## Installation

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cafe-management.git
cd cafe-management
```

### 2. Run Docker
```bash
docker compose up
```

### 3. Go to port http://0.0.0.0/
```bash
http://0.0.0.0/80 to see front
http://0.0.0.0/8088 to see back
```
everything loading through nginx 
in port http://0.0.0.0/8077 you can see without nginx
