# Pages Project

A website with a simple home page and about page.

## Topics Covered

* Templates - files which contain the HTML of a webpage. Generating an HTML response from within the view object/function does not scale beyond very simple sites like hello world. Templates allow Django to serve a predefined HTML file into which it can populate any custom information.

* Templates can be stored in a variety of places. By default, Django will look within the directory of each app for its corresponding templates. It expects the folder structure to be `./<app name>/templates/<app name>/<template name.html>`, which is quite cumbersome. Instead, a project-level folder can be created for templates and Django can be pointed towards it by editing the `settings.py` file. To do so, simply add the name of the folder to `TEMPLATES['DIRS']`

* Class-based views provide a more extensible/convenient way of defining views. Instead of having to define a function to output HTML, as in hello world, a view can take the form of a class which implements many common tasks for us. Custom functionality can be implemented by extending the members/functions of these classes.

* In order to display a simple template, we can define a view inheriting from the Django class `TemplateView` and set its `template_name` field to the name of the desired template file.