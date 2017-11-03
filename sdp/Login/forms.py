######### Author :  Nowshad #########

from django import forms
from django.contrib.auth.models import User
from django.views.generic import TemplateView,UpdateView

from .models import Student
from .fields import ListTextWidget

class LoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user_id', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class FormForm(forms.Form):
   filter_by_ = forms.CharField(required=True)

   def __init__(self,*args, **kwargs):

       _list = kwargs.pop('data_list', None) #####
       super(FormForm, self).__init__(*args, **kwargs)
       self.fields['filter_by_'].widget = ListTextWidget(data_list=_list, name='list') #####


class NameSearchForm(forms.Form):
    name = forms.CharField(label='Search by name', max_length=100)
