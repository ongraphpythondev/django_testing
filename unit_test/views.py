from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

def home(request):
    print("hii")
    all_posts = Post.objects.all()
    return render(request , "unit_test/index.html" , {"posts": all_posts})


def single_post(request , post):

    post = get_object_or_404(Post , slug = post)
    return render(request , "unit_test/detail.html" , {"post": post})
