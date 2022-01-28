from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=250)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("unit_test:single_post", args = [self.slug])
    


