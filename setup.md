Steps
-----

Create a virtual environment

    $ mkvirtualenv --python=/usr/local/bin/python3 pyconf_workshop

Create a directory for your codebase

    $ mkdir Pyconf
    $ cd Pyconf

Activate the virtual environment

    $ workon pyconf_workshop

Create a `requirements.txt` file with following libraries listed

    django
    djangorestframework
    psycopg2

Install the libraries

    $ pip install -r requirements.txt

Bootstrap the project

    $ django-admin startproject mysite

Create a database for this project

    ╰─$ psql
    psql (10.3)
    Type "help" for help.

    akshar=# create database pyconf_workshop;

Create a Django app

    $ cd mysite
    $ python manage.py startapp polls

Configure the database

    DATABASES = {
         'default': {
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME': 'pyconf_workshop',
            'USER': 'youruser',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        },
    }

Run migrations to ensure everything is running smoothly

    $ python manage.py migrate

This should create `auth` and `session` tables.

Add models `Question` and `Choice` to `polls`

Add `polls` to `INSTALLED_APPS`.

Makemigrations for polls

    $ python manage.py makemigrations

Migrate

    $ python manage.py migrate
