from django.contrib import admin

from .models import Doctor
from .models import DoctorVisit
from .models import Specialty
from .models import DoctorVisit

admin.site.registed(Address)
admin.site.register(Doctor)
admin.site.register(DoctorVisit)
admin.site.register(Specialty)
admin.site.register(DoctorVisit)

# Register your models here.
