from django.forms import ModelForm
from the_big_one.models import Address, Doctor

class AddressForm(ModelForm):
  class Meta:
    model = Address
    fields = ['street_address', 'city', 'state', 'zip_code']

class DoctorForm(ModelForm):
  class Meta:
    model = Doctor
    fields = ['first_name', 'last_name', 'email_address', 'phone_number']
