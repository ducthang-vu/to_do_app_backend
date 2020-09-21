# to_do_app_backend
**to_do_app_backend** is a python application which implements a basic API for a to-do app.

This project is still in development.

## Minimum requirements
This application is based on Django framework.

python==3.8.1

asgiref==3.2.10  
Django==3.1.1  
django-seed==0.2.2  
djangorestframework==3.11.1  
djangorestframework-simplejwt==4.4.0  
Faker==4.1.3  
mysqlclient @ file:///C:/mysqlclient-1.4.6-cp38-cp38-win32.whl  
PyJWT==1.7.1  
python-dateutil==2.8.1  
pytz==2020.1  
six==1.15.0  
sqlparse==0.3.1  
text-unidecode==1.3  


## Usage
Open terminal and install the necessary packages by running:

`pip install -r requirements.txt`

Then start the server by running:

`python manage.py runserver`

For running the tests, do:

`python manage.py test`


## Features 
The application works with two resources: users (id, username, first_name, email, password, tasks) and tasks (id, title, 
description, priority, completed).

Use the endpoint POST /users (parameters: username, first_name, email, password) to create a new user.

Use the endpoint POST /api/token/ (parameters: username, password) to get both the JWT token and the refresh token.
The JWT token expire after 5 minutes.

Use the endpoint POST /api/token/refresh/ with the refresh token to get a new JWT token.

Use the endpoint POST /api/tasks (header: ***Authorization: Bearer \<JWT token>***) to create a new task.
Use the endpoint GET|PUT|DELETE /api/tasks/\<id>/ (header: ***Authorization: Bearer \<JWT token>***) to perform 
CRUD actions (retrieve, update, delete) on tasks.
Use the endpoint GET /api/tasks (header: ***Authorization: Bearer \<JWT token>***) to get the list of all user's tasks.

Use the endpoint GET|PUT|DELETE api/users/\<id>/ (header: ***Authorization: Bearer \<JWT token>***) to perform 
CRUD actions (retrieve, update, delete) on user; user's first_name filed cannot be updated.
