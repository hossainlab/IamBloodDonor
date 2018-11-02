from django.db import models
from django.core.validators import URLValidator
from PIL import Image



class DonationProcess(models.Model):
    image       = models.ImageField()
    heading     = models.CharField(max_length=200)
    content     = models.TextField() 
    created_at  = models.DateTimeField(auto_now=True) 
    updated_at  = models.DateTimeField(auto_now=True)

class TeamMember(models.Model):
    image     = models.ImageField(default='team_member_photo')
    profile_name    = models.CharField(max_length=250)
    position        = models.CharField(max_length=200)
    facebook_link = models.CharField(validators=[URLValidator()], max_length=120)
    instagram_link = models.CharField(validators=[URLValidator()], max_length=120)
    twitter_link = models.CharField(validators=[URLValidator()], max_length=120)
    googleplus_link = models.CharField(validators=[URLValidator()], max_length=120)
    linkedin_link = models.CharField(validators=[URLValidator()], max_length=120)
    github_link = models.CharField(validators=[URLValidator()], max_length=120)

    def __str__(self):
        return self.profile_name

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class PhotoGallery(models.Model):
    image_author = models.CharField(max_length=250)
    image_title = models.CharField(max_length=250)
    image = models.ImageField(default='gallery')
    upload_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_title

    class Meta:
        ordering = ['-upload_time']



class Opinion(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    position = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)



class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()


class BloodRequestMessage(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True, null=True)


# Connected Organizations
class ConnectedOrganization(models.Model):
    choice_type = (
        ('Sponsor', 'Sponsor'),
        ('Organization', 'Organization')
    )
    organization_name = models.CharField(max_length=250)
    join_as = models.CharField(max_length=250, choices=choice_type)
    logo = models.FileField()
    web_link = models.CharField(validators=[URLValidator()], max_length=120)
    facebook_link  = models.CharField(validators=[URLValidator()], max_length=120)

    def __str__(self):
        return self.organization_name

class News(models.Model):
    name = models.CharField(max_length=250)
    news_text = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name