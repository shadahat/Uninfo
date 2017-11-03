######### Author :  Shahin #########

from django.contrib import admin
from .models import Student
from .models import Address
from .models import University
from .models import Department
from .models import School
from .models import College
from .models import Result
from .models import Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Address)
admin.site.register(University)
admin.site.register(Department)
admin.site.register(School)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Result)
