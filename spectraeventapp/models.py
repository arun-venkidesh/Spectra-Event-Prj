from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=55,unique=True)
    PhoneNumber=models.CharField(max_length=15)
    Password=models.CharField(max_length=50)

class EventRegistration(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=55)
    PhoneNumber=models.CharField(max_length=15)
    Category=models.CharField(max_length=50, choices=[('marriage','Marriage'), ('birthday','Birthday'), 
                                                      ('pre_wedding','PreWedding'), ('baby_shower','BabyShower'), 
                                                      ('bachelor_party','BachelorParty'),])
    
    EventType=models.CharField(max_length=50, choices=[('hindu_marriage', 'Hindu marriage'),('christian-marriage', 'Christian Marriage'), 
                                                       ('muslim_marriage', 'Muslim Marriage'),('child_birthday', 'Child Birthday'), 
                                                       ('infants', 'Infants'),('birthday_party', 'Birthday party'), ('My_birthday', 'My Birthday'), ('Friend_Birthday', 'Friend Birthday'), ('haldi', 'Haldi'), 
                                                       ('djvibes','DJVibes'), ('save_the_date', 'Save The Date'), ('ritual','Ritual'),
                                                       ('Musics_and_dance', 'Musics And Dance')])
    
    Date_and_Time=models.DateTimeField(null=True)
    Message=models.TextField()