from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTests(TestCase):


    def setUp(self):
        Post.objects.create(text='just a test')


    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}' # Python 3.6 "f string" which allows for variables between {}
                                              # to be directly inserted into strings
        self.assertEqual(expected_object_name, 'just a test')



class HomePageViewTest(TestCase):


    def setUp(self):
        Post.objects.create(text='this is another test')


    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home')) # reverse('name') searches the urls defined in the project
                                                # and returns the one with matching name
        self.assertEqual(resp.status_code, 200)


    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
