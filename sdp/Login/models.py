from django.db import models
from django.shortcuts import reverse


######### Author :  Noboni #########
class Address(models.Model) :
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    street_no = models.CharField(max_length=100,blank=True)
    house_no = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.city + " - " + self.area + " - " + self.country

    class Meta :
        unique_together = (('country','city','area','street_no','house_no'),)

######### Author :  Shahin #########
class University(models.Model) :
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

######### Author :  Shahin #########
class Department(models.Model) :
    name = models.CharField(max_length=100)
    university = models.ForeignKey('University',null=True)
    def __str__(self):
        return self.name + " - " + self.university.name
    class Meta :
        unique_together = (('name','university'),)


######### Author :  Shahin #########
class School(models.Model) :
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

######### Author :  Shahin #########
class College(models.Model) :
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name


######### Author :  Shahin #########
class Student(models.Model) :
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100,help_text = 'You can use small letters [a-z] and digits [0-9] only')
    password = models.CharField(max_length=100)

    mail_id = models.EmailField(max_length=100)
    dob = models.DateField(help_text = 'YYYY-MM-DD')

    department = models.ForeignKey('Department',null=True)

    school = models.ForeignKey('School', null=True)

    college = models.ForeignKey('College', null=True)

    year_of_enrollment = models.PositiveIntegerField( help_text = 'Use the following format: <YYYY>')

    address = models.ForeignKey('Address',null=True)

    profile_pic = models.FileField(blank=True,null=True)

    is_alumni = models.BooleanField(default=False)
    industry = models.CharField(max_length=100,blank=True)
    headline = models.CharField(max_length=200,blank=True)
    summary = models.CharField(max_length=200,blank=True)


    def __str__(self):
        return self.name + ' - ' + self.department.university.name

    ######### Author :  Noboni #########
    def get_absolute_url(self):
        return reverse('namesearch', kwargs={'pk': self.pk})


######### Author :  Noboni #########
class Course(models.Model):
    TYPE_CHOICES = [
        ("Theory", "Theory"),
        ("Lab", "Lab"),
    ]

    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    credit = models.FloatField()
    type = models.CharField(max_length=10,choices=TYPE_CHOICES, default="Theory")
    department = models.ForeignKey('Department',null=True)


    def __str__(self):
        return self.name + ' - ' + self.course_code

    class Meta :
        unique_together = (('course_code','department'),)

######### Author :  Noboni #########
class Result(models.Model):
    student = models.ForeignKey('Student')
    course = models.ForeignKey('Course')
    gpa = models.FloatField()

    def __str__(self):
        return self.student.name + ' - ' + self.course.name

    class Meta :
        unique_together = (('student','course'),)