from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from PIL import Image

# BloodGropModel
class BloodGroupName(models.Model):
    blood_group = models.CharField(max_length=20)

    def __str__(self):
        return self.blood_group

# DonorProfileModel
class Profile(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    donation_capability_choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    blood_group = models.ForeignKey(BloodGroupName, on_delete=models.CASCADE)
    location = models.CharField(max_length=120)
    institute = models.CharField(max_length=120, blank=True, null=True)
    occupation = models.CharField(max_length=120, blank=True, null=True)
    last_donation_date = models.DateField(blank=True, null=True)
    last_donation_place = models.CharField(max_length=50, blank=True, null=True)
    donation_capability = models.CharField(max_length=3, choices=donation_capability_choices, blank=True, null=True)
    phone = models.CharField(max_length=12)
    donation_times = models.IntegerField()
    facebook_link = models.CharField(validators=[URLValidator()], max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.name


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


