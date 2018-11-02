from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# All Models For BloodDonor App
from . models import (
    DonationProcess,
    PhotoGallery,
    TeamMember,
    DonationProcess,
    Opinion,
    BloodRequestMessage,
    ConnectedOrganization,
    News

)
from blog.models import BlogPost
# All Forms For BloodDonor App
from .forms import (
    ContactForm,
    PhotoUpload,
    OpinionForm,
    ConnectOrganizationForm,
    BloodRequestForm
)
from donor_profile.models import BloodGroupName


# HomeView
def index(request):
    posts = BlogPost.objects.all().order_by('-posted_on')[:2]
    photos = PhotoGallery.objects.all().order_by('-upload_time')
    members = TeamMember.objects.all()
    all_process = DonationProcess.objects.all()
    groups = BloodGroupName.objects.all()
    opinions = Opinion.objects.all().order_by('-created_at')
    blood_requests = BloodRequestMessage.objects.all().order_by('-date')[:3]
    organizations = ConnectedOrganization.objects.all().order_by('-organization_name')
    all_news = News.objects.all().order_by('-created_on')[:1]



    context = {
        'posts':posts,
        'photos': photos,
        'members': members, 
        'all_process': all_process,
        'groups': groups,
        'opinions': opinions,
        'blood_requests': blood_requests,
        'organizations': organizations,
        'all_news': all_news
    }
    return render(request, 'blooddonor/index.html', context)


# AboutView
def about(request):
    members = TeamMember.objects.all()
    context = {
        'members': members
    }
    return render(request, 'blooddonor/about.html')

# ContactView
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'blooddonor/contact.html', context)


# DonorOpinionView For Posting Donor Opinion
def opinion(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Opinion has been published successfully!')
            return redirect('home')
    else:
        form = OpinionForm()
    context = {
        'form':form
    }
    return render(request, 'blooddonor/opinion.html', context)

# PhotoGalleryView For Storing Donor's Photo
def photogallery(request):
    photos = PhotoGallery.objects.all()
    context = {
        'photos':photos
    }
    return render(request, 'blooddonor/gallery.html', context)

# PhotoUploadView For Uploading Photo
def photo_upload(request):
        if request.method == 'POST':
            form = PhotoUpload(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your photo has been uploaded successfully!')
                return redirect('home')
        else:
            form = PhotoUpload()
        context = {
            'form': form,
        }
        return render(request, 'blooddonor/photo_upload.html', context)

# ConnectOrganizationView
def connect_org(request):
    if request.method == 'POST':
        form = ConnectOrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your organization has been connected with us successfully!')
            return redirect('home')
    else:
        form = ConnectOrganizationForm()
    context = {
        'form': form,
    }
    return render(request, 'blooddonor/connect_organization.html', context)

# BloodRequest
def blood_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Message has been published! Hopefully You Will Get The ExpectedBlood Donor')
            return redirect('home')
    else:
        form = BloodRequestForm()
    context = {
        'form': form,
    }
    return render(request, 'blooddonor/blood_request.html', context)




def donation(request):
    process = DonationProcess.objects.all() 
    context = {
        'process':process
    }
    return render(request, 'blooddonor/index.html', context)