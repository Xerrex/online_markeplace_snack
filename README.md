# Online Marketplace 
* A marketplace made with django.

## Tools used
[Python](https://www.python.org/) - Programming language that lets you work quickly and integrate systems more effectively.

[Virtual Environment](https://virtualenv.pypa.io/en/stable/) - Tool to create isolated Python environments.

[Django](https://www.djangoproject.com/) - Framework that makes it easier to build better web apps more quickly and with less code.

[Sqlite](https://www.sqlite.org/index.html) - A small, fast, self-contained, high-reliability, full-featured, SQL database engine.

## Table of contents
* [Project apps](#project-apps)
* [Project setup & Run app](#project-setup--run-app)
* [Commands used](#commands-used)

## Project apps
* [conversation](./conversation/) - Handle web app conversations.
* [core_app](./core_app/) - Handle web app main page.
* [dashboard](./dashboard/) - Handles user managing marketplace items.
* [mkt_item](./mkt_item/) - Handle marketplace items.
* [project_core](./project_core/) -  Web app core.


## Project setup & Run app
* Setup virtual environment & activate
```
python3 -m venv venv
source venv/bin/activate
```

* Install dependencies
```
pip install -r requirements.txt
```

* Apply migrations
```
python manage.py migrate
```

* Run app
```
python manage.py runserver
```

* Visit web app on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Visit Admin web app on [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


## Commands used
* django-admin startproject project_core .
* python manage.py runserver
* python manage.py startapp core_app
* python manage.py startapp mkt_item
* python manage.py startapp dashboard
* python manage.py startapp conversation
* python manage.py makemigrations
* python manage.py migrate