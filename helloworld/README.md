# Hello World Project

A simple hello world project to get acquainted with the Django environment

## Topics covered

* Creating a project using `django-admin startproject` - `django-admin` is a CLI for Django (similar to what is used in Angular)

* `python manage.py` is another command-line interface for the actual application. Running `python manage.py runserver` will start up the development server (at localhost:8000). Additionally, `python manage.py startapp <app name>` can be used to set up a directory for a new app within the project.

* Each project will contain one or more "apps" which are responsible for specific pieces of functionality (eg. one app for user authentication, another for payments, a third for listing items etc.). Each app has its own configuration files, database models, and views. Apps used by the project must be added to the `INSTALLED_APPS` array in `<project dir>/settings.py` before Django will recognize them.

* Views define the content provided by an app. In this project it takes the form of a simple function which responds with 'Hello World' to any kind of request.

* In order for a client to access a view, it must be routed to a URL. Routing is a two-part process. First, the app itself must know which path to map to one of its views. This is declared under `urlpatterns` in `<app dir>/urls.py`. Each urlpattern contains three parts: a regular expression matching relevant URL paths, a reference to the view function/object, and an optional url name. Next, the project-wide URL router must be configured to point to the relevant app's routing configuration. This is declared under `urlpatterns` in `<project dir>/urls.py` and follows a similar pattern to the declaration in the app. However, instead of referencing a view, you reference the `urls.py` file of the app.
