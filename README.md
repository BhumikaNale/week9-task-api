
# Task Management REST API using Flask

## Project Overview

This project is a Task Management REST API developed using the Flask framework in Python. The application allows users to manage tasks through API endpoints. Users can register, log in, and perform operations such as creating, viewing, updating, and deleting tasks.

The system follows REST architecture principles and uses token-based authentication to secure protected routes.

---

## Objectives

The main objectives of this project are:

* To develop a RESTful API using Flask.
* To implement CRUD operations for task management.
* To integrate authentication using JSON Web Tokens (JWT).
* To store and manage data using a database.
* To test API functionality using an API testing tool.

---

## Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* SQLite Database
* Visual Studio Code
* Thunder Client (for API testing)

---

## Project Structure

```
week9-task-api/
│
├── task-api/
│   └── app.py
│
├── database.db
├── requirements.txt
└── README.md
```

---

## Setup and Installation

Follow these steps to run the project locally.

### 1. Clone the Repository

```
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate the virtual environment:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Required Dependencies

```
pip install flask flask_sqlalchemy flask_jwt_extended
```

Or if a requirements file is provided:

```
pip install -r requirements.txt
```

---

### 4. Run the Application

```
python task-api/app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

## API Endpoints

### User Authentication

| Method | Endpoint  | Description                    |
| ------ | --------- | ------------------------------ |
| POST   | /register | Register a new user            |
| POST   | /login    | Login and receive access token |

### Task Management

| Method | Endpoint    | Description              |
| ------ | ----------- | ------------------------ |
| POST   | /tasks      | Create a new task        |
| GET    | /tasks      | Retrieve all tasks       |
| GET    | /tasks/<id> | Retrieve a specific task |
| PUT    | /tasks/<id> | Update a task            |
| DELETE | /tasks/<id> | Delete a task            |

---

## Example Request

### Create Task

Endpoint:

```
POST /tasks
```

Header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Body:

```
{
  "title": "Complete Flask API project",
  "description": "Testing API",
  "priority": "High"
}
```

---

## Database

The project uses SQLite as the database. Two main tables are created:

### User Table

* id
* email
* password

### Task Table

* id
* title
* description
* status
* priority
* user_id

---

## Testing the API

All API endpoints were tested using Thunder Client inside Visual Studio Code. The tool allows sending HTTP requests and viewing responses for each endpoint.

