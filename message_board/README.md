# Message Board Application

A webpage displaying text stored in a database

## Topics Covered

* Database models are python objects which Django can map to tables in a database. Model objects inherit from a Django module called `models` and declare fields in which data will be stored. Each field must specify the type of data it will contain. For a simple string of text this project used `models.TextField()`, [but many other types are available](https://docs.djangoproject.com/en/2.0/ref/models/fields/).

* It is useful to implement the `__str__` function (analogous to `toString()` in Java) for database models. Often Django will want to display the information contained in a database model, and it will call this function to get a string representation of the model.

* Models are not incorporated into the database until they are "migrated". Doing this takes two steps. The first is to create a migration file by calling `python manage.py makemigrations <app_name>`. This file contains information on the actions Django will take to incorporate the models into the database. It serves to document what changes were made, and for that reason it should be kept small and specific. This means only a small set of model changes should be incorporated at a time, and each call to `makemigrations` should specify an `app_name`. To apply the migrations, call `python manage.py migrate <app_name>`. This will take the changes detailed in the migration file and execute them.

* Django admin is an interface for interacting with the database of a site. It allows authorized users to perform CRUD operations on the models contained in the database. To register an admin user run `python manage.py createsuperuser` and provide the necessary information. The admin can then log in through the `/admin` page.

* Before an admin can interact with a given model, it must be registered with the admin panel. An example of how to do this can be found in `posts/admin.py` with the main function call being `admin.site.register(<app_name>)`. From there, an admin can create, read, edit or delete database entries corresponding to the registered models.

* Creating a view to list database items is done by subclassing Django's `ListView` class. Simply define the relevant `model` and `template_name` fields (as in `posts/views.py`), and the view will provide an `object_list` variable to the template. This list contains all of the models currently present in the database.

* Iterating through items in a template can be done using `{% for <item> in <list> %} ... item.<field> ... {% endfor %}`. The HTML defined in the body of the loop will be repeated for each item in the list.

* To test a site backed by a database, a testing database must be initialized. This can be done from any class subclassing Django's `TestCase` class, and is implemented within a function called `setUp`. Here, database models are initialized and can be used in subsequent tests.
