Overview
This project is a full-stack web application for managing a store's inventory. It utilizes Nuxt 3 for the front end and Python for the back end.

Features:
View and manage products in the inventory
Add new products
Edit existing product details
Delete products
Authentication system for secure access
Role-based access control for admin and regular users

Technologies Used
Frontend:
Nuxt 3
Vue.js
Tailwind CSS
Backend:
Python
Django
Django REST Framework

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Node.js and npm
Python
Django
pipenv

Installation Frontend
1.Clone the repository:
git clone https://github.com/ashutosh164/assignment-storemanagement.git

2. Navigate to the project directory:
cd assignment-storemanagement

Install frontend dependencies:
1. naviget to frontend command : cd frontend
2. install module command : npm install
3. run frontend command: npm run dev
4. onle 3 working url for frontend
   1. http://localhost:3000/inventory
   2. http://localhost:3000/login
   3. inventory add and edit http://localhost:3000/inventory/id (this page only accessble for Store manager)
   

install backend dependencies:
1. create a virtual environment
2. active virtual environment
3. install dependencies command:-- pip install -r requirements.txt
4. cd backend
5. migrate data base command := python manage.py migrate
6. you can create supperuser to access the admin:= python manage.py createsuperuser
8. run backend command:= python manage.py runserver
   
   
   

   
   


