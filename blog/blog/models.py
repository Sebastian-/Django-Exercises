from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User', # reference to the built in Django user model
        on_delete=models.CASCADE, # this option specifies that when an author model is deleted,
                                  # all of their associated posts are also deleted
    )
    body = models.TextField()


    def __str__(self):
        return self.title
