# Blog Application

## Topics Covered

### Part 1

In this part, the model for posts is created and views for the homepage and single-post pages are defined.

* New types of fields were introduced when defining the posts model:
    * [`CharField`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#charfield) holds a string which is expected to be limited to a certain number of characters. This differs from `TextField` which does not limit its string length.
    * [`ForeignKey`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#foreignkey) defines a many-to-one relationship between models. In this case it is the relationship between posts and their authors. In using this relationship, it is implied that an author may be related to many posts, but a post will only have a single author. This relationship also takes an `on_delete` argument, which dictates what should happen to the database entry of the post if its foreign key author entry is deleted.

* Static files are files that stay the same regardless of the application's state. Examples include CSS stylesheets or images. Ordinarily you would use a CDN (content delivery network) to serve these files, but they can also be stored locally. To do so, create a folder to contain the files, then add `STATICFILES_DIRS = [<folder_path>]` to `settings.py`. In order to reference static files within a template, load it by calling `{% load <folder_name> %}` at the top of the file.

* A `DetailView` is another class-based view provided by Django. It is useful when displaying pages for a single instance of a database model. To use it, simply provide a model class and template name, and the class will make a "context object" available inside the template. This object can be referenced inside the template by either the lowercase version of the model's class name, or simply as `object`. Alternatively, the name can be set by assigning one to the `context_object_name` field of the view.

* The `DetailView` object must be provided with information about which database model it should provide to the template. This information is transmitted via a URL. When declaring the url pattern for a `DetailView` object, include a variable parameter inside the path's regular expression. The value of the variable will be used to retrieve the corresponding model from the database. For posts, the path was declared as `post/<int:pk>/`, where `pk` corresponds to the primary key of the post. By default, Django will add a primary key (which acts as a unique identifier) to any model we declare. This field can then be used to uniquely reference any instance of a model.

* To construct a parameterized url within a template, call `{% url <'url_name'> <desired_value_of_parameter> %}`.
