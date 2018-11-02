from django.contrib import admin
# All Models From BloodDonor App
from . models import (
    DonationProcess ,
    PhotoGallery,
    TeamMember,
    Contact,
    Opinion,
    BloodRequestMessage,
    ConnectedOrganization,
    News
)

# BloodDonation Process ModelAdmin and Register
class DonationProcessAdmin(admin.ModelAdmin):
    list_display = ['heading']
admin.site.register(DonationProcess, DonationProcessAdmin)

# DonorOpnionAdmin and Register
class OpinionAdmin(admin.ModelAdmin):
    list_display = ['name','created_at', 'position']
admin.site.register(Opinion, OpinionAdmin)



# PhotoGalleryAdmin and Register
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['image_author','image_title', 'upload_time', 'image']
admin.site.register(PhotoGallery, PhotoGalleryAdmin)

# TeamMemberModelAdmin and Register
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['profile_name', 'position']
admin.site.register(TeamMember,TeamMemberAdmin )

# ContactAdmin and Register
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
admin.site.register(Contact, ContactAdmin)

class BloodRequestMessageAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(BloodRequestMessage, BloodRequestMessageAdmin)

# Connected Organizations
class ConnectedOrganizationAdmin(admin.ModelAdmin):
    list_display = ['organization_name','join_as','logo', 'web_link', 'facebook_link']
admin.site.register(ConnectedOrganization, ConnectedOrganizationAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on']
admin.site.register(News, NewsAdmin)