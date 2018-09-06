# Blog Application

## Topics Covered

### Part 1

In this part the model for posts is created and views for the homepage and single-post pages are defined

* New types of fields were introduced when defining the posts model:
    * [`CharField`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#charfield) holds a string which is expected to be limited to a certain number of characters. This differs from `TextField` which does not limit its string length.
    * [`ForeignKey`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#foreignkey) defines a many-to-one relationship between models. In this case it is the relationship between posts and their authors. In using this relationship, it is implied that an author may be related to many posts, but a post will only have a single author. This relationship also takes an `on_delete` argument, which dictates what should happen to the database entry if its foreign key entry is delete.