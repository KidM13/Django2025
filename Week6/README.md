# Requirements and Setup
## Requirements

Python 3.10 or higher

Git

Virtual environment support (venv)

Django

## Clone the repository
git clone <your-repository-url>
cd <project-folder>

## Create a virtual environment
python -m venv venv

## Activate the virtual environment
## Windows (Git Bash / PowerShell)
source venv/Scripts/activate

## Windows (Command Prompt)
venv\Scripts\activate

## Linux / macOS
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Run migrations
python manage.py makemigrations
python manage.py migrate

## Start development server
python manage.py runserver
