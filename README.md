# To-Do App 
A simple To-Do application built with Flask and Python. It allows users to organize daily tasks, set priorities and deadlines. This project is my part of practice which helping me to learning web-development with Python, working with Flask, integration of database and templates of html.

## Features
- **Task Management:** Add tasks with a title, multi-line description, priority level (Low, Medium, High), and a specific due date and time.
- **Deadline Tracking:** Server-side calculation checks task deadlines and displays visual status indicators—showing an "Overdue!" badge in red, a breakdown of hours and minutes if due within 24 hours, or days remaining.
- **Search & Filter:** Search tasks instantly by title and filter views by all, pending, or completed status.
- **Sorting:** Sort task lists by default ID order, due date, or priority level.
- **Flash Feedback:** Instant notification alerts when tasks are added successfully[cite: 5, 6].



## Technologies Used:
- Python--core application logic and datetime management
- Flask--web framework
- Flask-SQLAlchemy--database ORM integration
- SQLite--lightweight relational database
- Jinja-- template inheritence 
- HTML--page structure
- Bootstrap-- responsive styling, cards, badge and forms

## Project Structure
To-Do App/
├── app.py
├── models.py
├── requirements.txt
├── .gitignore
└── templates/
    └── index.html

## Getting Started
### 1. Clone the repository
        git clone https://github.com/Asadullah-Mim/todo-app.git
        cd todo-app

### 2. Create a virtual environment
        python -m venv .venv

### 3. Activate the virtual environment
        On Windows Powershell:
        .venv\Scripts\Activate.ps1

### 4. Configure environment variables
        Create a .env file in the root directory set a secret key:
        SECRET_KEY=your_secret_key_here

### 6. Install dependencies
        python -m pip install -r requirements.txt

### 7. Run the application
        flask --app app run

Open the local address shown in your terminal, usually http://127.0.0.1:5000/, in your browser.

**Note:**
The repository contains the application code and dependencies. You may need to initialize the database according to the setup in app.py before running the app for the first time.

## What I Learned
- Building a web appliation with Flask
- Connecting a Flask application to SQLite using Flask-SQLAlchemy
- Organizing templates and application files
- Using Git and GitHub for version control

## Author 
### Asadullah Mim

GitHub: Asadullah-Mim