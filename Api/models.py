from django.db import models

# Create your models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('Construction','Construction'),
                                                  ('Automobile','Automobile'),
                                                  ('Interior','Interior'),
                                                  ('MNC','MNC'),
                                                  ('Law Firm','Law Firm'),
                                                  ('Gaming','Gaming')))
    about=models.TextField(default='null')
    date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    address=models.CharField(max_length=200)
    about=models.TextField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    position=models.CharField(max_length=100,choices=(('manager','Manager'),
                                                      ('SDE','Software Developer'),
                                                      ('PDE','Python Developer'),
                                                      ('Director','Director'),
                                                      ('AI/ML','AI/ML Developer'),
                                                      ('HR','HR'),
                                                      ('EP','Entrepreneur'),
                                                      ('CE','Civil Engineer'),
                                                      ('Law','Lawyer'),
                                                      ('TL','Team Leader'),
                                                      ('ME','Mechanical Engineer'),
                                                      ('ECE/EEE','Electronics or Electrical Engineer'),
                                                      ('CA','Accountant'),
                                                      ('BA','Business Analyst'),
                                                      ('DA','Data Analyst'),
                                                      ('CEO','Chief Executive Officer')
                                                      ))
    date_of_joining=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
