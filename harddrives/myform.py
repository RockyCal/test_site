from django import forms
from django.core.exceptions import ObjectDoesNotExist
from harddrives import models
from harddrives.models import File, Box, Employee , Harddrive

class FileForm(forms.Form):
    name = forms.CharField()
    def is_valid(self):
        valid = super(FileForm, self).is_valid()
        if not valid:
            return valid
        cd = self.cleaned_data
        try:
            File.objects.get(name=cd['name'])
        except ObjectDoesNotExist:
            return False
        return True

class HarddriveForm(forms.Form):
    serial_number = forms.CharField()
    box=forms.ModelChoiceField( queryset=Box.objects.all(), required=False)
    person=forms.ModelChoiceField( queryset=Employee.objects.all(),
                required=False)
    def is_valid(self):
        valid = super(HarddriveForm, self).is_valid()
        if not valid:
            return valid
        cd = self.cleaned_data
        if ( ( cd['box'] is None ) == ( cd['person'] is None ) ):
            return False
        return True;
        
class CheckoutForm(forms.Form):
    serial_number = forms.CharField()
    box=forms.ModelChoiceField( queryset=Box.objects.all(),
                initial='Checkin',
                required=False)
    person=forms.ModelChoiceField( queryset=Employee.objects.all(),
                initial='Checkout',
                required=False)
    def is_valid(self):
        valid = super(CheckoutForm, self).is_valid()
        if not valid:
            return valid
        cd = self.cleaned_data
        if ( ( cd['box'] is None ) == ( cd['person'] is None ) ):
            return False
        try:
            Harddrive.objects.get(serial_number=cd['serial_number'])
        except ObjectDoesNotExist:
            return False
        return True;
