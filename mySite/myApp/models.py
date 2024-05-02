from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class PatientProfile(models.Model):

    def __str__(self):
        return self.fName+self.lName

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=18)
    note = models.CharField(max_length=300, blank=True)
    pID = models.CharField(max_length=15)
    bloodGroup = models.CharField(max_length=6)
    isDoctor = models.BooleanField(default=False)
    isManager = models.BooleanField(default=False)
    isPatient = models.BooleanField(default=True)
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)

class DoctorProfile(models.Model):

    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=18)
    note = models.CharField(max_length=300)
    dID = models.CharField(max_length=15)
    isDoctor = models.BooleanField(default=True)
    isManager = models.BooleanField(default=False)
    isPatient = models.BooleanField(default=False)
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30, default="ENT")



class ManagerProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=18)
    note = models.CharField(max_length=300)
    mID = models.CharField(max_length=15)
    isDoctor = models.BooleanField(default=False)
    isManager = models.BooleanField(default=True)
    isPatient = models.BooleanField(default=False)
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)


class Slot(models.Model):

    def __str__(self):
        return str(self.id)

    status = models.CharField(max_length=20)
    patient = models.ForeignKey(PatientProfile,on_delete=models.CASCADE)

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=40)
    reason = models.CharField(max_length=20)
    
    referal = models.BooleanField(default=False)
    referredFrom = models.CharField(max_length=30,blank=True)
