from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.db.models.deletion import CASCADE, DO_NOTHING
import datetime


# class CustomUser(AbstractUser):
#     pass

# Create your models here:

class Foster(models.Model):
    class Meta:
        verbose_name_plural = 'fosters'
        
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='change_this_email@nowhere.com')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
        
    def __str__(self):    
        return '%s %s' % (self.first_name, self.last_name)
    
class Cat(models.Model):
    SITE_CHOICES = (
    ("NONE", "None"),
    ("GARAGE", "Garage"),
    ("ADOPTCTR", "AdoptCtr"),
    ("FOSTER", "Foster"),
    )
    ROOM_CHOICES = (
    ("NONE", "None"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),    
    ("6", "6"),
    )  
    name = models.CharField(max_length=100, unique=True)
    foster = models.ForeignKey(
        Foster,
        related_name='cats',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    location = models.CharField(
        max_length=8,
        choices = SITE_CHOICES,
        default = 'NONE'
    )
    room_num = models.CharField(
        max_length=8,
        choices = ROOM_CHOICES,
        default = 'NONE'
    )
    class Meta:       
        verbose_name_plural = 'cats'  
    
    def __str__(self):
        return f"{self.name}"
    
class Vet(models.Model):

    vet_name = models.CharField(max_length=100)
    practice_name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    cats = models.ManyToManyField(Cat, related_name='vets', through='Vetvisit')
    
    class Meta:
        verbose_name_plural = 'vets'
        unique_together = ('vet_name', 'practice_name')

    def __str__(self):
        return f"{self.vet_name}"

    
# Many to Many relationship bridge tables with added fields. 

class VetVisit(models.Model):
    cat = models.ForeignKey(Cat, null=True, on_delete=models.SET_NULL, related_name='cats')
    vet = models.ForeignKey(Vet, null=True, on_delete=models.SET_NULL, related_name='vets')
    date_visited =models.DateField()
    next_appt_date = models.DateField()
    problem = models.CharField(max_length=256, blank=True)
  
    
    
    def __str__(self):
        
        return "Cat: %s , Date of visit: %s , Vet: %s" % (self.cat, self.date_visited, self.vet)

class Medication(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    prescribed_to = models.ManyToManyField(Cat, related_name='medications', through='Prescription')
    prescribed_by = models.ManyToManyField(Vet, related_name='medications', through='Prescription')
    
    def __str__(self):
        return f"{self.name}"

class Prescription(models.Model):
    cat = models.ForeignKey(Cat, related_name='prescriptions', null=True, on_delete=models.SET_NULL)
    vet = models.ForeignKey(Vet, related_name='prescriptions', null=True, on_delete=models.SET_NULL )
    med = models.ForeignKey(Medication, related_name='prescriptions',  null=True, on_delete=models.SET_NULL)
    date_prescribed = models.DateField()
    prescription_num = models.PositiveIntegerField(unique=True, blank=False)
    dosage = models.CharField(max_length=100, blank=False)
    frequency = models.CharField(max_length=100, blank=False)
    instructions = models.CharField(max_length=512, blank=True, default='')
                                  
    def __str__(self):
        
        return "%s, %s, %s, %s" % (self.cat, self.med, self.vet, self.prescription_num)