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
