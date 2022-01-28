from django.test import TestCase
from ..models import Post

class Post_testcase(TestCase):
    def test_model_str(self):
        title = Post.objects.create(title = "For checking" , content = "this is content")
        self.assertEqual(str(title) , "For checking")