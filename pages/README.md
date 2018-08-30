# Pages Project

A website with a simple home page and about page.

## Topics Covered

* Templates are files which contain the HTML of a webpage. Generating an HTML response from within the view object/function does not scale beyond very simple sites like hello world. Templates allow Django to serve a predefined HTML file which it can populate with custom information.

* Templates can be stored in a variety of places. By default, Django will look within the directory of each app for its corresponding templates. It expects the folder structure to be `./<app_name>/templates/<app_name>/<template_name.html>`, which is quite cumbersome. Instead, a project-level folder can be created for templates and Django can be pointed towards it by editing the `settings.py` file. To do so, simply add the name of the folder to `TEMPLATES['DIRS']`

* Templates can be extended using Django's templating language (very similar to Jinja templates, which were actually inspired by Django). A template can extend another template by declaring `{% extends '<parent_template.html>' %}`. This will have the effect of including all of the content defined in the parent template. The child template can insert its own content within "blocks" defined by the parent. Blocks are declared with `{% block <block_name> %} {% endblock %}` and a child template can insert its content between the two brace statements. See `templates/base.html` and `templates/home.html` for an example of a parent/child template relationship.

* Class-based views provide a more extensible/convenient way of defining views. Instead of having to define a function to output HTML, as in hello world, a view can take the form of a class which implements many common tasks for us. Custom functionality can be implemented by extending the members/functions of these classes.

* In order to display a simple template, we can define a view inheriting from the Django class `TemplateView` and set its `template_name` field to the name of the desired template file.

* Tests are defined for each app in the `tests.py` file of their respective folder. Each route's response can be obtained and compared with the desired output. See `pages/tests.py` for examples of simple tests which check for a 200 status code.
