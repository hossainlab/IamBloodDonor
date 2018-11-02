from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from . models import BloodGroupName, Profile


# All Forms For DonorProfile Views
from .forms import (
    RegisterDonorForm,
    LoginForm,
    UserSignUpForm
)

# BloodGroupView For Displaying All Blood Groups
def bloodgroup(request):
    groups = BloodGroupName.objects.all()
    context = {
        'groups':groups
    }
    return render(request, 'donor_profile/blood_group.html', context)

# DonorProfileView
@login_required
def add_donor(request):
    if request.method == 'POST':
        form = RegisterDonorForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, f'Congratulations! Your account has been created successfully.Now you are able to donate blood')
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = RegisterDonorForm()
    context = {
        'form': form
    }
    return render(request, 'donor_profile/add_donor.html',context)

@login_required
def profile(request):
    try:
        donor = Profile.objects.get(user=request.user)
        context = {
            'donor': donor,
             }
        return render(request, 'donor_profile/donor_detail.html', context)
    except:
        return render(request, 'donor_profile/create_profile.html')


def register(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, f'Your password is nor correct! Please type your correct password')
                context = {
                    'form':form
                }
                return render(request, 'donor_profile/signup.html', context)
            User.objects.create_user(username, email, password)
            messages.success(request, f'Your registration has been completed! Please Login and Create Your Profile')
            return redirect('donor-login')
    else:
        form = UserSignUpForm()
    context = {
        'form':form
    }
    return render(request, 'donor_profile/register.html', context)




# DonorListView For Individual BLoodGroups
def donor_list(request, bgname):
    donors = Profile.objects.filter(blood_group__blood_group=bgname)
    search = request.GET.get('q')
    if search:
        donors = donors.filter(
            Q(location__icontains=search)|
            Q(institute__icontains=search)|
            Q(donation_capability__icontains=search)
        )
    paginator = Paginator(donors, 5)
    page = request.GET.get('page')
    donors = paginator.get_page(page)
    context = {
        'donors':donors,
        'bgname':bgname
    }
    return render(request, 'donor_profile/donor_list.html', context)


# DonorDetailView
def donor_detail(request,id):
    donor = Profile.objects.get(id=id)
    context = {
        'donor': donor
    }
    return render(request, 'donor_profile/donor_detail.html', context)


# DonorLoginVIew
def donor_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('add-donor')
                # messages.error(request, f'Password or Username Invalid!')
    else:
        form = LoginForm()
    context = {
        'form':form
    }
    return render(request, 'donor_profile/donor_login.html', context)

# DonorLogoutView
def donor_logout(request):
    logout(request)
    messages.success(request, f'You are logged out!')
    return redirect('home')

# DonorProfileEditView
@login_required
def edit_profile(request):
    select = Profile.objects.get(user = request.user)
    form = RegisterDonorForm(request.POST or None, instance=select)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, f'Your Account Has Been Updated Successfully!')
            return redirect('donor-detail', id= post.id)

    context = {
        'form':form
    }
    return render(request, 'donor_profile/edit_profile.html', context)

# DonorProfileEditView
@login_required
def delete_profile(request, id):
    select_donor = Profile.objects.get(id=id)
    select_donor.delete()
    messages.success(request, f'Your account has been deleted!')
    return redirect('home')


