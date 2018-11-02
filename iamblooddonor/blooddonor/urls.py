from django.urls import path
from . import views
# BloodDonorApp's URL
urlpatterns = [
    path("",views.index, name='home'),
    path("about/",views.about, name='about'),
    path("contact/",views.contact, name='contact'),
    path('connect/', views.connect_org, name='connect-organization'),
    path("photogallery",views.photogallery, name="gallery"),
    path('photo_upload/', views.photo_upload, name='photo-upload'),
    path('opinion/', views.opinion, name='opinion'),
    path('blood_request/', views.blood_request, name='blood-request'),
    path("donation/",views.donation, name='donation'),
]
