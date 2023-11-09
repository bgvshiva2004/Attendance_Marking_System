from django.db import models


def upload_photo(instance,filename):
      return f'uploads/{filename}'
# Create your models here.
class ClassImage(models.Model):
    course_choices = [
        ('None', 'Select'),
        ('MA 205', 'MA 205'),
        ('CS 201', 'CS 201'),
        ('CS 203', 'CS 203'),
        ('CS 207', 'CS 207'),
    ]
    course = models.CharField(max_length=20, choices=course_choices,default='CS 203')
    date = models.CharField(max_length=100)
    image=models.ImageField(upload_to=upload_photo)
    def __str__(self):
            return self.date

class Attendance_record(models.Model):
    year_choices = [
        ('None', 'Select'),
        ('B.Tech I', 'B.Tech I'),
        ('B.Tech II', 'B.Tech II'),
        ('B.Tech III', 'B.Tech III'),
        ('B.Tech IV', 'B.Tech IV'),
        ('M.Tech I', 'M.Tech I'),
        ('M.Tech II', 'M.Tech II'),
    ]

    department_choices = [
        ('None', 'Select'),
        ('CSE', 'Computer Science Engineering'),
        ('MnC', 'Mathematics and Computing Science Engineering'),
        ('EE', 'Electrical Engineering'),
        ('SE', 'Space Science Engineering'),
        ('EP', 'Engineering Physics'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('ChE', 'Chemical Engineering'),
        ('MEMS', 'Metallurgical and Material Science Engineering'),
    ]

    course_choices = [
        ('None', 'Select'),
        ('MA 205', 'MA 205'),
        ('CS 201', 'CS 201'),
        ('CS 203', 'CS 203'),
        ('CS 207', 'CS 207'),
    ]

    year = models.CharField(max_length=20, choices=year_choices,blank=True,null=True)
    department = models.CharField(max_length=50, choices=department_choices,blank=True,null=True)
    course = models.CharField(max_length=20, choices=course_choices,blank=True,null=True)
    date = models.CharField(max_length=100,blank=True,null=True)
      

class embeddings(models.Model):
    embeddings = models.FileField()
      