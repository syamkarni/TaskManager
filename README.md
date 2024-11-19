# Task Manager Application

A web-based task management application built with Flask (backend), Vue.js (frontend), and SQLite (database). This application provides an intuitive interface to create, view, update, delete, and mark tasks as complete, with secure token-based authentication.

---

## Features

- **Task Management**:
  - Add tasks with a title, description, due date, and status.
  - View all tasks in a list.
  - Update task details.
  - Mark tasks as complete.
  - Delete tasks.

- **Authentication**:
  - Secured API endpoints using token-based authentication.

- **Dynamic Updates**:
  - Real-time updates of the task list without needing to reload the page.

---

## Technologies Used

### Backend:
- **Flask**: Python-based web framework for building the RESTful API.
- **Flask-SQLAlchemy**: Object Relational Mapper for database operations.
- **Flask-CORS**: Cross-Origin Resource Sharing to handle requests from the frontend.
- **SQLite**: Lightweight database for storing tasks.

### Frontend:
- **Vue.js**: JavaScript framework for creating a responsive user interface.
- **Axios**: HTTP client for communication with the backend.

---

## Installation Instructions

### Prerequisites
- Python 3.7+ installed.
- Node.js and npm installed.

### Clone the Repository
```bash
git clone https://github.com/syamkarni/TaskManager
cd TaskManager

```
---

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install flask flask-sqlalchemy flask-cors
   ```
4. Start the Flask server:
   ```bash
   python3 main.py
   ```
5. The backend will be running at `http://127.0.0.1:5000`.

---

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install npm dependencies:
   ```bash
   npm install
   ```
3. Start the Vue.js development server:
   ```bash
   npm run serve
   ```
4. The frontend will be running at `http://localhost:8080`.

---

## API Endpoints

| Method | Endpoint                | Description                |
|--------|-------------------------|----------------------------|
| GET    | `/tasks`                | Retrieve all tasks         |
| GET    | `/tasks/<id>`           | Retrieve a specific task by ID |
| POST   | `/tasks`                | Create a new task          |
| PUT    | `/tasks/<id>`           | Update an existing task    |
| DELETE | `/tasks/<id>`           | Delete a task              |
| PATCH  | `/tasks/<id>/complete`  | Mark a task as complete    |

---

## Authentication

- **Token**: The backend requires a token to access the API endpoints.
- Include the following header in all API requests:
  ```plaintext
  Authorization: Bearer mysecrettoken
  ```

---

## Testing

### Running Tests
A test suite is included to verify the functionality of the backend API.

1. Ensure the backend is set up and all dependencies are installed.
2. Run the test script:
   ```bash
   python3 test_app.py
   ```



### Test Coverage
- **Create Task**: Ensures a new task can be added.
- **Get Tasks**: Verifies all tasks are retrieved correctly.
- **Mark Task Complete**: Confirms tasks can be marked as complete.

---