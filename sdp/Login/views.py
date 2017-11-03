from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import *
from .Iterator import *
from .template_method_pattern import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .Decoratorpattern import *
from abc import ABC

#########################################################
#########################################################
#            Strategy and State Pattern                 #
#########################################################
#########################################################


######### Author :  Noboni + Shahin #########
class abstractview(ABC,TemplateView) :
    def __init__(self):
        pass
    def get(self, request):
        pass
    def post(self, request):
        pass


# home page extending abstract view class, part of Strategy Pattern
class index(abstractview):
    form_class = FormForm
    template_name = 'signup.html'
    list = ('University', 'School', 'College')

    def get(self, request):
        form = self.form_class( data_list=self.list)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, data_list=self.list)
        if form.is_valid():
            data = form.cleaned_data.get('filter_by_')

            # changing states , part of State Pattern

            if data == "University":
                return redirect('universitysearch')
            elif data == "School":
                return redirect('schoolsearch')
            elif data =="College":
                return redirect('collegesearch')

        return render(request, self.template_name, {'form': form})


# login redirect page extending abstract view class, part of Strategy Pattern
class LoginRequest(abstractview):
    form_class = LoginForm
    template_name = 'signin.html'

    def get(self,request):

        form=self.form_class(None)

        return render(request,self.template_name, {'form':form})

    def post(self,request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user_id = form.cleaned_data.get('user_id')

            password = form.cleaned_data.get('password')

            myTable = Student.objects.all()


            #########################################################
            #            Using Iterator Pattern                     #
            #########################################################

            s = Iterator(myTable)

            bool = False

            while s.hasnext():

                k = s.next()

                if k.user_id == user_id and  k.password == password:
                    bool=True
                    result = Result.objects.filter(student=k)

                    grade_point = 0.0
                    total_credit = 0.0

                    list = [['Course Name', 'GPA']]

                    for r in result:
                        grade_point += r.course.credit * r.gpa
                        total_credit += r.course.credit

                        list.append([r.course.name, r.gpa])

                    if total_credit == 0.0:
                        cgpa = 0.0
                    else:
                        cgpa = grade_point / total_credit

                    cgpa = round(cgpa, 2)

                    context = {
                        'student': k,
                        'result': result,
                        'cgpa': cgpa,
                        'list': list,
                    }


                    #########################################################
                    #            Calling Decorator Pattern                  #
                    #########################################################

                    concrete_component = ConcreteComponent(request, context, 'profile.html')
                    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
                    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)

                    return concrete_decorator_b.operation()
            if bool == False:
                return render(request, self.template_name, {'form': form})


# page consisting list of universities , A class of State Pattern , Child of abstractview

class UniversitySearch(abstractview):
    form_class = FormForm
    template_name = 'universitysearch.html'

    searcher = UniversitySearcher()
    list = searcher.search()
    model = University.objects.all()
    def get(self, request,*args, **kwargs):
        form = self.form_class(data_list=self.list)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list']=self.list
        context['model'] = self.model
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, data_list=self.list)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list'] = self.list
        context['model'] = self.model
        if form.is_valid():
            data = form.cleaned_data.get('filter_by_')
            s = Iterator(self.model)
            while s.hasnext():
                d = s.next()
                if d.name == data:
                    k=d.id
                    return HttpResponseRedirect(reverse('departmentsearch', args=(k,)))

        return render(request, self.template_name, context)



# page consisting list of departments , A class of State Pattern , Child of abstractview

class departmentbasesearch(abstractview):
    form_class = FormForm
    template_name = 'departmentsearch.html'

    searcher = DepartmentSearcher()
    list = searcher.search()
    model = Department.objects.all()

    def get(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        list1 =[]
        for k in self.model:
            if k.university.id == unid:
                list1.append(k.name)

        form = self.form_class(data_list=list1)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list']=self.list
        context['list1']=list1
        context['unid'] = unid
        context['model']= self.model
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        list1 =[]
        for k in self.model:
            if k.university.id == unid:
                list1.append(k.name)
        form = self.form_class(request.POST, data_list=list1)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list'] = self.list
        context['list1'] = list1
        context['unid'] = unid
        context['model'] = self.model
        if form.is_valid():
            data = form.cleaned_data.get('filter_by_')
            s = Iterator(self.model)
            while s.hasnext():
                k= s.next()
                if k.university.id == unid:
                    if k.name == data:
                        j = k.id
                        return HttpResponseRedirect(reverse('unamesearch', args=(j,)))
        return render(request, self.template_name, context)



# A state of State Pattern extending abstractview class

class unamesearch(abstractview):
    form_class = FormForm
    template_name = 'namesearch.html'
    model = Student.objects.all()

    def get(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        list1 = []
        for k in self.model:
            if k.department.id == unid:
                list1.append(k.name)
        form = self.form_class(data_list=list1)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list1'] = list1
        context['unid'] = unid
        context['model'] = self.model
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        list1 = []
        for k in self.model:
            if k.department.id == unid:
                list1.append(k.name)
        form = self.form_class(request.POST, data_list=list1)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list1'] = list1
        context['unid'] = unid
        context['model'] = self.model
        if form.is_valid():
            data = form.cleaned_data.get('filter_by_')

            #########################################################
            #            Using Iterator Pattern                     #
            #########################################################

            iterable = Iterator(self.model)
            while iterable.hasnext():
                object = iterable.next()
                if object.department.id == unid:
                    if object.name == data:
                        j = object.id
                        return HttpResponseRedirect(reverse('namesearch', args=(j,)))
        return render(request, self.template_name, context)




# A state of State Pattern extending abstractview class

class Collegesearch(abstractview):
    form_class = FormForm
    template_name = 'collegesearch.html'

    searcher = CollegeSearcher()
    list = searcher.search()
    model = College.objects.all()

    def get(self, request, *args, **kwargs):
        form = self.form_class(data_list=self.list)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list'] = self.list
        context['model'] = self.model
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, data_list=self.list)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list'] = self.list
        context['model'] = self.model
        if form.is_valid():
            data = form.cleaned_data.get('filter_by_')

            #########################################################
            #            Using Iterator Pattern                     #
            #########################################################

            iterable = Iterator(self.model)
            while iterable.hasnext():
                d = iterable.next()
                if d.name == data:
                    k = d.id
                    return HttpResponseRedirect(reverse('collegestudents', args=(k,)))


        return render(request, self.template_name, context)


# A state of State Pattern extending abstractview class

class cnamesearch(abstractview):
    form_class = FormForm
    template_name = 'cnamesearch.html'
    model = Student.objects.all()

    def get(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        list1 = []
        for k in self.model:
            if k.college.id == unid:
                list1.append(k.name)
        print(list1)
        form = self.form_class(data_list=list1)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list1'] = list1
        context['unid'] = unid
        context['model'] = self.model
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        list1 = []
        for k in self.model:
            if k.department.id == unid:
                list1.append(k.name)
        form = self.form_class(request.POST, data_list=list1)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list1'] = list1
        context['unid'] = unid
        context['model'] = self.model
        if form.is_valid():
            data = form.cleaned_data.get('filter_by_')

            #########################################################
            #            Using Iterator Pattern                     #
            #########################################################

            iterable = Iterator(self.model)
            while iterable.hasnext():
                k = iterable.next()
                if k.college.id == unid:
                    if k.name == data:
                        j = k.id
                        return HttpResponseRedirect(reverse('namesearch', args=(j,)))
        return render(request, self.template_name, context)




class Schoolsearch(abstractview):
    form_class = FormForm
    template_name = 'schoolsearch.html'

    searcher = SchoolSearcher()
    list = searcher.search()
    model = School.objects.all()

    def get(self, request, *args, **kwargs):
        form = self.form_class(data_list=self.list)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list'] = self.list
        context['model'] = self.model
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, data_list=self.list)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list'] = self.list
        context['model'] = self.model
        if form.is_valid():
            data = form.cleaned_data.get('filter_by_')

            #########################################################
            #            Using Iterator Pattern                     #
            #########################################################

            iterable = Iterator(self.model)
            while iterable.hasnext():
                d = iterable.next()
                if d.name == data:
                    k = d.id
                    return HttpResponseRedirect(reverse('schoolstudents', args=(k,)))
        return render(request, self.template_name, context)

class snamesearch(abstractview):
    form_class = FormForm
    template_name = 'snamesearch.html'
    model = Student.objects.all()

    def get(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        print(unid)
        list1 = []
        for k in self.model:
            if k.school.id == unid:
                list1.append(k.name)
        print(list1)
        form = self.form_class(data_list=list1)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list1'] = list1
        context['unid'] = unid
        context['model'] = self.model
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        list1 = []
        for k in self.model:
            if k.department.id == unid:
                list1.append(k.name)
        form = self.form_class(request.POST, data_list=list1)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['list1'] = list1
        context['unid'] = unid
        context['model'] = self.model
        if form.is_valid():
            data = form.cleaned_data.get('filter_by_')

            #########################################################
            #            Using Iterator Pattern                     #
            #########################################################

            iterable = Iterator(self.model)
            while iterable.hasnext():
                k = iterable.next()
                if k.school.id == unid:
                    if k.name == data:
                        j = k.id
                        return HttpResponseRedirect(reverse('namesearch', args=(j,)))

        return render(request, self.template_name, context)



class basicprofile(abstractview):
    def get(self, request, *args, **kwargs):
        unid = int(kwargs.pop('pk', None))
        myTable = Student.objects.all()
        s = Iterator(myTable)
        while s.hasnext():
            k = s.next()
            if k.id ==unid:
                result = Result.objects.filter(student=k)

                grade_point = 0.0
                total_credit = 0.0

                list = [['Course Name', 'GPA']]

                for r in result:
                    grade_point += r.course.credit * r.gpa
                    total_credit += r.course.credit

                    list.append([r.course.name, r.gpa])

                if total_credit == 0.0:
                    cgpa = 0.0
                else:
                    cgpa = grade_point / total_credit

                cgpa = round(cgpa, 2)

                context = {
                    'student': k,
                    'result': result,
                    'cgpa': cgpa,
                    'list': list,
                }

                concrete_component = ConcreteComponent(request,context,'basicprofile.html')
                concrete_decorator_a = ConcreteDecoratorA(concrete_component)
                concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)

                return concrete_decorator_b.operation()

class UpdateProfile(UpdateView) :
    model = Student
    fields = ['name', 'mail_id', 'dob', 'school' , 'college', 'address' , 'industry' , 'headline' , 'summary' ]



import MySQLdb
import json

@login_required
def home(request) :

    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="qwe123",
                           db="UniDB")

    cursor = conn.cursor()

    cursor.execute("select extra_data from social_auth_usersocialauth")

    data = cursor.fetchall()

    print(cursor.rowcount)

    data = str(data[cursor.rowcount-1][0])

    print(data.__len__())


    data = json.dumps(data)
    data = json.loads(data)
    data = json.loads(data)

    full_name = data['first_name'] + " " +  data['last_name']

    students = Student.objects.all()

    #########################################################
    #              Using Iterator Pattern                   #
    #               Linkedin Data Update                    #
    #########################################################

    iterable = Iterator( students )

    while iterable.hasnext():

        student = iterable.next();

        if student.name == full_name :

            student.summary = data['summary']
            student.headline = data['headline']
            student.country = data['location']['name']
            student.industry = data['industry']

            student.summary = data['summary']
            student.headline = data['headline']
            student.address.country = data['location']['name']
            student.industry = data['industry']


            student.save()

            break

    return render( request , 'error.html' )