# E-Book Library
The E-Book Library is a web application for managing and browsing a collection of e-books. It allows users to upload, categorize, and view e-books in an organized manner.

# Features
*User Authentication:* Secure user authentication system with registration and login.

*Book Management:* Add, edit, and delete e-books. Each e-book includes details such as title, author, cover image, category, and more.

*Category Filtering:* Easily filter and browse e-books by category.

*Search Functionality:* Search for e-books by title, author, or keywords.

*User Profiles:* User profiles with the ability to upload a profile picture and view their uploaded e-books.

*Admin Panel:* Admin panel for managing e-books and user accounts.

# Getting Started
These instructions will help you set up and run the E-Book Library project on your local machine.

# Prerequisites
- Python (3.6+)
- Django (3.0+)
- SQLITE# (or another database of your choice)
- Git

# Installation
Step 1: pip install virtualenv

Step 2: virtualenv env

Step 3: cd env/Scripts

Step 4: activate

Step 5: cd ../..

Step 6: pip install django

Step 7: python manage.py makemigrations

Step 8: python manage.py migrate –run-syncdb

Step 9: python manage.py createsuperuser

Step 10: python manage.py runserver

Step 11: Access the admin panel at http://localhost:8000/admin/ and log in with the superuser account created               earlier to add e-books and manage the site.

Step 12: Access the site at http://localhost:8000/ to browse and search for e-books.
