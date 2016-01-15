from django.conf.urls import url

from . import views
from the_big_one.views import DoctorListView, DoctorDetailView

# The intention here is that they go to .../doctors to search for doctors, see a
# list of doctors etc. They then go to .../doctors/2 to see the details of an
# individual doctor

# This is fed from www.medron.org/core
urlpatterns = [
    url(r'^$', views.core_404_page, name='core_404'),
    url(r'^doctors/*$', DoctorListView.as_view(), name = "doctor-list"),
    url(r'^doctors/(?P<pk>[0-9]+)/$', 
            DoctorDetailView.as_view(), 
            name='doctor'),

    ]

# points to FBV for doctor index if I ever need it
#    url(r'^doctors($|\/$)', views.doc_index, name='doc_index'),

# points to FBV for doctor detail
#    url(r'^doctors/(?P<doctor_id>[0-9]+)/$', views.doctor, name='doctor'),

