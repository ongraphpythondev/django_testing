from django.test import SimpleTestCase
from django.urls import reverse , resolve
from ..views import home , single_post

class TestUrls(SimpleTestCase):

    def test_home(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func , home)


    def test_detail(self):
        url = reverse('single_post' , args = ['some-slug'])
        self.assertEqual(resolve(url).func , single_post)