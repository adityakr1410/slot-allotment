
from django.urls import path
from .views import *

urlpatterns = [
    path('check/',check,name='check'),
    path('deskManager/',deskLandingPage,name='deskManager'),
    path('doctorLogin/',doctorLogin,name='doctorLogin'),
    path('managerLogin/',managerLogin,name='managerLogin'),
    path('patientLogin/',patientLogin,name='patientLogin'),
    path('register/',register,name='register'),
    path('addPatient/',addPatient,name='addPatient'),
    path('bookSlotDesk/',bookSlotDesk,name='bookSlotDesk'),
    path('doctorsDashboard/<str:val>',doctorsDashboard,name='doctorsDashboard'),
    path('managersDashboard/',managersDashboard,name='managersDashboard'),
    
        
    
]
