from django.contrib import admin

from .models import Doctor
from .models import DoctorVisit
from .models import Specialty
from .models import Address

admin.site.register(Address)
admin.site.register(Doctor)
admin.site.register(DoctorVisit)
admin.site.register(Specialty)

# Register your models here.
