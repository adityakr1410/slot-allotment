from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
import datetime

from collections import defaultdict

# Create your views here.


def check(request):
    return HttpResponse("Hello")


def deskLandingPage(request):
    return render(request,'deskLandingPage.html')

def patientLogin(request):
    return render(request,'patientLogin.html')

def doctorLogin(request):
    return render(request,'doctorLogin.html')

def managerLogin(request):
    return render(request,'managerLogin.html')

def register(request):
    if request.method=='POST':
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return redirect('check')

    user_form = UserRegistrationForm()
    return render(request,'register.html',{'user_form':user_form})

@login_required
def addPatient(request):

    if (request.method=="POST"):
        user = request.user
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        bloodGroup = request.POST.get('bloodGroup')
        f_Name = request.POST.get('fName')
        l_Name = request.POST.get('lName')

        patient = PatientProfile(user=user,age=age,gender=gender,phone=phone,note=note,bloodGroup=bloodGroup,fName=f_Name,lName=l_Name)
        patient.save()
        print("adasda")
        return render(request,'addPatient.html')

    return render(request,'addPatient.html')


def bookSlotDesk(request):
    
    if(request.method == 'POST'):
        ph = request.POST.get('phone')
        patient = PatientProfile.objects.get(phone=str(ph))
        reason = request.POST.get('reason')
        date = request.POST.get('date')
        date=date.split('-')
        date2 = date[2]+"-"+date[1]+"-"+date[0]
        doctor = request.POST.get('doctorOption')
        dName = doctor.split(" ")
        doctor = DoctorProfile.objects.get(fName=dName[0],lName=dName[1])
        slot = Slot(status="wait", patient=patient, doctor=doctor,date=date2,reason=reason)
        slot.save()

        return redirect('/bookSlotDesk/')

    context={}
    doctors = DoctorProfile.objects.all()
    
    slots = Slot.objects.all()
    patientCountPerDoctor = defaultdict(int)
    
    docs = DoctorProfile.objects.all()

    docLst=[]
    for x in docs:
        docLst.append(x.fName+" "+x.lName)

    context['docLst']=docLst

    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y")

    count=0
    for slot in slots:
        # print(today==slot.date)
        if today==slot.date:
            patientCountPerDoctor[slot.doctor]+=1
            count+=1
    print(patientCountPerDoctor)

    context['today']=count
    context['patientCount']=dict(patientCountPerDoctor)
    return render(request,"bookSlotDesk.html",context)


def doctorsDashboard(request,val):
    context={}
    
    forward = Slot.objects.filter(referal=True)
    slots = Slot.objects.filter(referal=False)
    patientsCount = PatientProfile.objects.all().count()
    doctorsCount = DoctorProfile.objects.all().count()
    managersCount = ManagerProfile.objects.all().count()
    slotsCount = Slot.objects.all().count()

    context['slots']=slots
    context['forwards']=forward
    context['forwardCount']=len(forward)
    context['totalSlots']=len(slots)+len(forward)
    context['totalPatients']=patientsCount
    context['totalStaff']=doctorsCount+managersCount
    context['totalSlots']=slotsCount


    if('none' in val):
        val=False

    else:
        current = Slot.objects.get(id=int(val))
        context['current']=current
        val=True
    context['view']=val
    return render(request,'doctorsDashboard.html',context)


def managersDashboard(request):
    context={}

    slots = Slot.objects.all()
    context['totalSlots']=len(slots)

    today = datetime.date.today()
    date1 = today.strftime("%d-%m-%Y")
    todaySlotCount = 0
    for slot in slots:
        if(slot.date==date1):
            todaySlotCount+=1            
    context['todaysCount']=todaySlotCount

    doctors = DoctorProfile.objects.all()
    context['doctorCount'] = len(doctors)
    context['doctors'] = doctors

    patients = PatientProfile.objects.all()
    context['patients'] = patients

    slots = Slot.objects.filter(status="wait")
    context["slots"] = slots

    return render(request,'managersDashboard.html',context)