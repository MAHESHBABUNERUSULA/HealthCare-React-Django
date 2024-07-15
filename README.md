# Healthcare Management System

## Description
A comprehensive Healthcare Management System built using React, Bootstrap, Django, and MySQL. This application facilitates efficient patient management, appointment scheduling, medical records handling, billing, and insurance claims management. It ensures a responsive design suitable for both desktop and mobile views.

## Key Features
- **Patient Management:** Add, view, and manage patient records.
- **Appointment Scheduling:** Schedule and manage patient appointments.
- **Medical Records:** Securely store and retrieve patient medical records.
- **Billing:** Manage patient billing and generate invoices.
- **Insurance Claims:** Process and track insurance claims efficiently.
- **Responsive Design:** Implemented using Bootstrap, ensuring compatibility across various devices.

## Technologies Used
- React (Frontend)
- Bootstrap (Frontend)
- Axios (Frontend)
- Django (Backend)
- MySQL (Database)

## Setup and Installation

### Frontend
1. Navigate to the `healthcare-frontend` directory:
   ```sh
   cd healthcare-frontend
2. Install frontend dependencies:
  ```sh
   npm install
3. Start the frontend development server:

npm start
Backend
Navigate to the healthcare-backend directory:

cd healthcare-backend
Set up a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install backend dependencies:
pip install -r requirements.txt
Run database migrations:
sh
Copy code
python manage.py migrate
Start the backend development server:
sh
Copy code
python manage.py runserver
