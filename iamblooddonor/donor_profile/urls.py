from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

# All URLS For DonorProfileApp
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.donor_login, name='donor-login'),
    path('logout/', views.donor_logout, name='donor-logout'),
    path("add_donor/", views.add_donor, name='add-donor'),
    path("profile/", views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit-profile'),
    path('delete_profile/<int:id>/', views.delete_profile, name='delete-profile'),
    path('donor_list/<bgname>/', views.donor_list, name='donor-list'),
    path('donor_detail/<int:id>/', views.donor_detail, name='donor-detail'),
    path('bloodgroups/', views.bloodgroup, name='bloodgroup'),

]

