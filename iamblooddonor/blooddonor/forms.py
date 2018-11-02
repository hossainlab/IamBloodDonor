from django import forms
from .models import (
    Contact,
    PhotoGallery,
    Opinion,
    ConnectedOrganization,
    BloodRequestMessage
)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class PhotoUpload(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = '__all__'


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = '__all__'


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequestMessage
        fields = '__all__'

class ConnectOrganizationForm(forms.ModelForm):
    class Meta:
        model = ConnectedOrganization
        fields = '__all__'