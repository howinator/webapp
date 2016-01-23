from django.db import models
from localflavor.us.models import USZipCodeField
from localflavor.us.models import USStateField
from localflavor.us.models import PhoneNumberField


class Address(models.Model):
    street_address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
    state = USStateField(max_length=2)
    zip_code = USZipCodeField(max_length=10)
    is_active = models.BooleanField(
        verbose_name='is address actively being used',
        default=True)
    user_submitted = models.BooleanField(default=False)

    # Two time stamp fields
    # auto_now_add time stamps when it is first created
    date_entered = models.DateTimeField(
        verbose_name='date+time address entered',
        auto_now_add=True)
    # auto_now time stamps when the field is saved
    date_last_updated = models.DateTimeField(
        verbose_name='date+time last changed',
        auto_now=True)

    def __str__(self):
        full_address = '''
        {address}
        {city},
        {state} {zip_code}
    '''.format(
              address=self.street_address,
              city=self.city,
              state=self.state,
              zip_code=self.zip_code)
        return full_address


class Specialty(models.Model):
    # A model for storing the available specialties
    # TODO Refine the many-to-many replationship to express the membership of a
    # doctor in a specialty more effectively

    specialty_name = models.CharField(max_length=250)

    def __str__(self):
        return self.specialty_name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # a doctor has one address, but multiple doctors can have same address
    # therefore, many-to-one replationship
    address = models.ForeignKey(Address, blank=True, null=True)
    # doctor can have multiple specialties and specialties can belong to
    # multiple doctors therefore, many-to-many relationship
    specialties = models.ManyToManyField(Specialty)
    email_address = models.EmailField()
    phone_number = PhoneNumberField(max_length=9)
    # This field should be automatically calculated by a script nightly
    average_price = models.DecimalField(max_digits=10,
                                        blank=True, null=True, decimal_places=2)
    date_entered = models.DateTimeField(
        verbose_name='date+time doctor entered',
        auto_now_add=True)
    date_last_updated = models.DateTimeField(
        verbose_name='date+time last changed',
        auto_now=True)

    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return name


class DoctorVisit(models.Model):
    doctor = models.ForeignKey(Doctor)
    address = models.ForeignKey(Address)
    visit_date = models.DateTimeField('Date of Visit')
    procedure = models.CharField('Procedure', max_length=250)
    price = models.DecimalField('Price', decimal_places=2, max_digits=9)

    def showPrice():
        return '$' + str(self.price)

    def __str__(self):
        doctor_string = str(self.doctor)
        address_string = str(self.address)
        full_output = '''
      Doctor : {doctor}

      Address : {address}

      Date of Visit : {visit_date}

      procedure : {procedure}

      price : {price}
    '''.format(
            doctor_string=str(self.doctor),
            address_string=str(self.address),
            visit_date=str(self.visit_date),
            procedure=self.procedure,
            price=self.showPrice())
        return full_output
