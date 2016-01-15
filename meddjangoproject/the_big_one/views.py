from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Doctor

class DoctorListView(ListView):

  model = Doctor
  template_name = "doctors/doctor_list.html"
  context_object_name = "submitted_doctors"

class DoctorDetailView(DetailView):

  model = Doctor
  template_name = "doctors/doctor_detail.html"


# TODO This needs to get turned into an actual 404 page that re-directs to
# either doctors or doctor visits
def core_404_page(request):
  return HttpResponse("Oops! This page doesn't exist. Please navigate to \
  another page.")


# Deprecated FBVs below this line

# FBV for showing Doctor Detail
#def doctor(request, doctor_id):
#  doctor = get_object_or_404(Doctor, pk=doctor_id)
#
#  return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})


# FBV for doctor listing in case I ever need it
# Takes variable number of argumnets because the trailing slash from the url 
# gets fed to the view function
# def doc_index(request, *arg):
#  latest_doctor_list = Doctor.objects.order_by('-date_entered')[:5]
#  context = {'latest_doctor_list': latest_doctor_list}
#  return render(request, 'doctors/index.html', context)

