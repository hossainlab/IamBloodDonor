from django.contrib import admin
from . models import BloodGroupName, Profile

# BloodGroupNameAdmin
class BloodGroupNameAdmin(admin.ModelAdmin):
    list_display = ['blood_group']
admin.site.register(BloodGroupName, BloodGroupNameAdmin)

# ProfileAdmin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'blood_group', 'phone', 'last_donation_date', 'donation_capability']
admin.site.register(Profile, ProfileAdmin)