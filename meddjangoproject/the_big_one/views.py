# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.

from .models import Doctor

def index(request):
  latest_doctor_list = Doctor.objects.order_by('-date_entered')[:5]
  context = {'latest_doctor_list': latest_doctor_list}
  return render(request, 'doctors/index.html', context)

def doctor(request, doctor_id):
  doctor = get_object_or_404(Doctor, pk=doctor_id)
  return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})

