Simple Notes App
A minimal, full-stack application for creating, viewing, updating, and deleting notes. This project demonstrates a clear separation of concerns, utilizing React with Vite for a modern, responsive frontend and Django to provide a robust RESTful API and persistent data storage.

✨ Features
Create: Quickly add new notes with a title and content.

Read: View a list of all existing notes.

Update: Edit the content of any stored note.

Delete: Permanently remove notes from the database.

Responsive Design: Optimized layout for both desktop and mobile devices.

🚀 Tech Stack
Component

Technology

Description

Frontend

React.js (via Vite)

UI Library for building the user interface.

Styling

CSS/Tailwind CSS

Used for rapid, responsive styling (Assumed).

Backend

Django

Python web framework for application logic.

API

Django REST Framework (DRF)

Used to build the standardized RESTful API endpoints.

Database

SQLite

Default database for local development.

⚙️ Prerequisites
Before you begin, ensure you have the following installed on your system:

Python (3.8+): For running the Django backend.

pip: Python package installer.

Node.js (18+): For running the React frontend.

npm or yarn: Package manager for Node.js.

📦 Installation and Setup
Follow these steps to get the application up and running on your local machine.

1. Clone the Repository
git clone [YOUR_REPO_URL]
cd simple-notes-app

2. Backend Setup (Django)
The backend handles the API and database operations.

Navigate to the backend directory:

cd backend

Create and activate a virtual environment:

# Create environment (optional, but highly recommended)
python -m venv venv

# Activate environment (Linux/macOS)
source venv/bin/activate

# Activate environment (Windows)
.\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

(Assuming a requirements.txt file exists containing Django, djangorestframework, etc.)

Apply database migrations:

python manage.py makemigrations
python manage.py migrate

Start the Django server:

python manage.py runserver

The backend API will now be running at http://localhost:8000.

3. Frontend Setup (React + Vite)
The frontend serves the user interface and interacts with the Django API.

Navigate to the frontend directory:

cd ../frontend

Install Node dependencies:

npm install
# or
yarn install

Start the development server:

npm run dev
# or
yarn dev

The React application should now be accessible in your web browser, typically at http://localhost:5173.

💡 Usage
Open your browser and navigate to http://localhost:5173.

The application will automatically fetch any existing notes from the Django backend.

Use the input fields and buttons to create, edit, and delete notes.

Ensure both the Django server (http://localhost:8000) and the Vite development server (http://localhost:5173) are running simultaneously for the app to function correctly.
