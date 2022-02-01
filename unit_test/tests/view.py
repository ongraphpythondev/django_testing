from turtle import title
from django.test import TestCase , Client
from django.urls import reverse , resolve
from ..models import *


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.detail_url = reverse('single_post' , kwargs={'s': "corona"})
        self.title = Post.objects.create(title = "corona" , content = "this is content")


    def test_home(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , "unit_test/index.html")

    def test_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , "unit_test/detail.html")

    
    def test_dh(self):
        response = self.client.get(reverse('single_dj' , kwargs={"s":"corona"}))

        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , "unit_test/detail.html")

        

