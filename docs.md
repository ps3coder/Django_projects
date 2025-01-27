2. Course Overview

3. What is Django

PBKDF2
SHA-256

4. Why should we use Django ?

• Built with python programming language
• Data science , Ai , ML , web Application
• Admin pannel
• Django ORM
• Dont repeat yourself principle
• Scalable and relible
• Security
• Open source

5. Software installation

6. Virtual Environment Overview

• Inside the Virtual Environment we actually install specific versions of the package to run our application.

• If we dont create virtual environment then we will install the package globally.

• Suppose if we install Django 3.1 and after for other project we install Django4.0 Then at that time we will face some problems. and thats why our project will crash due to version mismatch.

7. Creating and activating virtual environment

9. Project Structure


django-admin startproject mysite .

python manaage.py runserver


file structure :


Manage.py :

 •its a command line utility that is let you to interact with django project in various ways.
 • So we can think of this file as a tool for executing many django specific tasks by running django commands.
 • For running the development server we use python manage.py runserver.

for changing the password we use python manage.py changepassword with username

for creating the tables we use a python manage.py migrations and migrate commands.

db.sqlite3 : Database configuration file

mysite directory :

most of the files are located in this directory. 

packgaes : a folder that contains the python modules or python files.

• __init__.py : use to import one package to another which is usefull for this task. We can say those importing things happens because of this file.

• wsgi.py and asgi.py(comes with additional fetures) : wsgi(web server gateway interface) and asgi(Asynchronus server gateway interface) server for deploying our django application on the apache server and nginx server.
• urls.py : provide address of the resources. images webpages and websites.

• settings.py:use to  Adding all configuration settings for the project.

--> App level file structure

10. Django settings explained

BASE_DIR : For getting root directory dynamically.

SECRET_KEY : For generation of hashes and tokens. : django-insecure-50digit secret key.


DEBUG : True or False(boolean). : for debugging purpose.
• don't run with debug turned on in production!



ALLOWED_HOSTS : For putting the IP address of the server or hosts.

INSTALLED_APPS : Multiple apps , you must regitser in this section if we create any app

MIDDLEWARE : For adding the middleware classes like verifications.

ROOT_URLCONF : for addressing urls.py file in the main directory

TEMPLATES: For adding the templates


WSGI_APPLICATION : where to run the wsgi server(advance stuff)


DATABASES : For adding the database configuration.


AUTH_PASSWORD_VALIDATORS : built in password validators enusure to check the password strength.


LANGUAGE_CODE

TIME_ZONE

USE_I18N : Internationalization(The way of making our application to be used in multiple languages)

USE_TZ : time zone

STATIC_URL : 

DEFAULT_AUTO_FIELD :


11. How exactrly django works ?

django follows the model , view , template (MVT) architecture.

MODEL : responsible for each and every database realted operation.
If you want to do anything related to the satbase then you must contact this model.

Template : So the template is basically a user facing front end layout which can be html or bootstrap.

View : View acts as  a bridge between the template and the model.
a function where we write a logic

view can access the database

• urls.py : inbuilt funtion path and include.


check if the urls exist or not then provide the view function and response.


function will contain logic in views and return the response. 
and send a request to model if the given request exist then the model provide info to the view function.

13. URL's and HTTP Response

basic request and response 


go to urls.py

create a new function in views.py 
and return something


14. Implement Django templates

so go to the settings.py file and add the path or name(templates) in 

TEMPLATES = [
'DIRS': [],
]

15. Implementing Bootstrap

CDN - content delivery network

16. Django Static files

STATIC_ROOT = BASE_DIR / 'static'


STATICFILES_DIRS =[
    'mysite/static'
]


1. StaticURL: So Static URl is the URL which will serve those static files.

StaticROOT :

Collect static files for deployment or use.

StaticFiles :
we can add static files to our project by using the staticfiles app. and we can add also some more static files.

17. Django Apps

A django app is a python package that is speicifically meant for using in a Django project.

basically it is a seprate submodule of a project.


$ python manage.py startapp employees

for creating specific fetures we use apps.

in employees folder we have 

admins.py : Where we can manage the basic CRUD operations.

apps.py : this file is created to help the user to add any application level configuration for this app. // no need to make changes

models.py : this file is used to create the database models.
behaviour of the database.

tests.py : this file is used to perform the unit testing.

views.py : this file is used to write the logic.


18. Dajango Admin panel

python manage.py createsuperuser

[admin](http://127.0.0.1:8000/admin/) 

19. creating a model

we will store some data in datbase.



19. Media files

# Media file configuration

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


in the urls.py add the media url

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


20. Fetch from database

so first import models from Employees 

then use in def function of views.py to print the  employees details.

(split tags) or template tags

jango template variables --> Used to display the data in the template. which are in python
code.

template filters --> used to modify the data.


20. Git setup

git commit - m "message" : to commit the changes
