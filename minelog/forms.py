from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Schools,Students

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email','username','password1','password2')



class Member(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'username' ,}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'realname'}))
    school = forms.ModelChoiceField(queryset=Schools.objects.all(), to_field_name='School_Name',required=True,widget=forms.Select(attrs={'class':'Schoolname'}))
    code = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'code'}))
    rule_choices = Students.Rule_CHOICES
    rule = forms.ChoiceField(choices=rule_choices, required=True, widget=forms.Select(attrs={'class': 'rule'}))