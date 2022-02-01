from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

def home(request):
    print("hii")
    all_posts = Post.objects.all()
    return render(request , "unit_test/index.html" , {"posts": all_posts})


def single_post(request , s):

    post = get_object_or_404(Post , title = s)
    return render(request , "unit_test/detail.html" )



def single_dj(request , s):

    post = get_object_or_404(Post , title = s)
    return render(request , "unit_test/detail.html" )
