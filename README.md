# Student Task Manager

A complete beginner-friendly Python + Django web application.

## Features
- Register, log in, and log out
- Create, edit, delete, and complete tasks
- Set task priority and deadline
- Dashboard with task counts
- Each user sees only their own tasks
- SQLite database and Django admin

## Requirements
- Python 3.10 or newer
- Internet connection for installing Django and loading Bootstrap from its CDN

## Run on Windows

Open Command Prompt in this folder and run:

```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py makemigrations tasks
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

Admin page: http://127.0.0.1:8000/admin/

## Push to GitHub

Create an empty repository on GitHub, then run these commands from this project folder:

```bat
git init
git add .
git commit -m "Initial Student Task Manager project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your own GitHub repository URL. Do not commit passwords, secret keys, or your local database.

This is a development project. Before public production deployment, set DEBUG=False, configure a private SECRET_KEY, configure ALLOWED_HOSTS, use HTTPS, and follow Django's deployment checklist.
