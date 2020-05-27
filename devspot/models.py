from django.db import models
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('Date Published')
    slug = models.SlugField(max_length=200, default='How to code')
    author = models.CharField(max_length=50, default='DevSpot')
    image = models.ImageField(default='default.jpg', upload_to='pimages')

    def __str__(self):
        return self.title

class profile(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='aimages')

    def __str__(self):
        return self.name
