from django.db import models
from donor_profile.models import Profile
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from PIL import Image

class Category(models.Model):
    category_title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_title

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image  = models.ImageField(upload_to='blog-images')
    title       = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content     = models.TextField()
    status      = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Draft ')
    posted_on   = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    updated_on  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


    def save(self):
        super().save()

        img = Image.open(self.featured_image.path)

        if img.height > 360 or img.width > 230:
            output_size = (360, 230)
            img.thumbnail(output_size)
            img.save(self.featured_image.path)
