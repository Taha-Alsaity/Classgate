from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login , logout , get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
import sys
from django.contrib.auth.models import User
from .forms import RegisterUserForm
from . import urls
from .models import Schools, Students, ExamMark, Content,Exam,ExamQ
# Create your views here.
from django.contrib.auth.models import User
import datetime
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from random import randint
from .forms import Member
from django.core.exceptions import ObjectDoesNotExist






def main(request):
    Total = Students.objects.count()
    return render(request,'index/Taha-21.html',{
        'usersss'  : User.objects.count(),
        'total':Total
     
     
    })
    


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if   'log-ar/' in  request.META.get('HTTP_REFERER')  :
                messages.success(request,f'مرحبا !{request.user.username} استمتع بوقتك')
                return redirect('user-ar')
            elif  'log-en/' in  request.META.get('HTTP_REFERER') :
                messages.success(request,f'Welcome {request.user.username} enjoy your time')
                return redirect('userr')
        else:
            messages.error(request,'Wrong email or password, try again')
            return redirect('log')
    else:
        return render(request,'index/log in.html',{
            'url': request.META.get('HTTP_REFERER')
        })



def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user )
            messages.success(request,('sucsses'))
            return redirect('log')
    else:
        form = RegisterUserForm()
    return render(request,'index/register.html',
    {'form':form,
     'url': request.META.get('HTTP_REFERER'),
     'url1': '/log-ar'
     })
    

        

def userr(request):
    Total = Students.objects.count()
    if request.user.username == (''):
        messages.error(request,'Page not found')
        return redirect('main')
    else:
        return render(request,'index/user.html',{
     'usersss'  : User.objects.count(),
        'total':Total
    })
    



def membership(request):
    schs = Schools.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['mail']
       
        
        try:
            member = Students.objects.get(name=name,email=email)


            

            
            messages.success(request, f"you are a member of {member.school} your code is {member.password}")

            return render(request, 'index/member.html',{
            'code': not None,
            'form':Member()
            })
        except Students.DoesNotExist:
                member=None
                messages.error(request, "Invalid member user try again laterr")

                return render(request, 'index/member.html',{
                'code': "Nonev",
                "schs": schs
                })

    return render(request, 'index/member.html',{
'code': None
})

def join(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['mail']
        School = request.POST['sch']
        passw= randint(100000,999999)
        sch= Schools.objects.get(School_Name=School)
        # not allowed to be teacher only (S) or student
        try:
            existing_student = Students.objects.get(name=name)  # Check if name already exists
            messages.error(request, "Name is already taken")
            return render(request, 'index/member.html', {
                'code': "Nonev",
                "schs": Schools.objects.all()
            })
        except ObjectDoesNotExist:
            pass  # Name is unique, continue to next step

        try:
            existing_student = Students.objects.get(password=passw)  # Check if password already exists
            messages.error(request, "Password is already taken")
            return render(request, 'index/member.html', {
                'code': "Nonev",
                "schs": Schools.objects.all()
            })
        except ObjectDoesNotExist:
            pass  # Password is unique, continue to next step
        if sch.flex == 'Pr':
            messages.error(request, "Cant join, this School is private.")
            return render(request, 'index/member.html', {
                'code': "Nonev",
                "schs": Schools.objects.all()
            })
        else:
            std = Students(name=name,email=email,school=sch,password=passw,rule="S")
            std.save()
            member = Students.objects.get(name=name,email=email)
            messages.success(request, f"you are a member of {member.school.School_Name} your code is {member.password}")

            return render(request, 'index/member.html',{
            'code': not None,
            'form':Member()
            })
    

    return render(request, 'index/member.html',{
    'code': "Nonev",
    "schs": Schools.objects.all()
    })

    
def code(request):
    if request.user.username == (''):
        return render(request,'index/Error.html',{})
    else:
        if request.method == 'POST':
            form = Member(request.POST)
            if form.is_valid():
                
                
                realname = form.cleaned_data['name']
                code = form.cleaned_data['code']
                schooll = form.cleaned_data['school']
                rulle = form.cleaned_data['rule']

                try:
                    student1 = Students.objects.get(name=realname)

                    if  realname == student1.name  and code == student1.password and schooll == student1.school  and student1.rule == rulle  and student1.rule == "S" :
                       request.session['my_name'] = student1.name
                       messages.success(request,f"{student1.name}  You are a Member of {student1.school.School_Name} school")
                       return redirect(f'{student1.school.School_Name}-Student')

                    elif realname == student1.name  and code == student1.password and schooll == student1.school  and student1.rule == rulle  and student1.rule == "T" :
                       request.session['my_name'] = student1.name
                       messages.success(request,f"{student1.name}  You are a Member of {student1.school.School_Name} school")
                       return redirect(f'{student1.school.School_Name}-Teacher')

                    else:
                         messages.error(request, "Invalid member user try again later")
                         return render(request, 'index/member.html',{
                         'form':Member()
                          })
                except Students.DoesNotExist:
                  messages.error(request, "Invalid member User try again later")

        return render(request, 'index/member.html',{
            'form':Member()
        })


def logout_user(request):
    logout(request)
    if 'user-AR' in  request.META.get('HTTP_REFERER') or '-ar' in request.META.get('HTTP_REFERER') :
        messages.success(request,("لقد قمت بتسجيل الخروج بنجاح !!" ))
        return redirect('m-ar')
    elif 'user-EN' in  request.META.get('HTTP_REFERER') or 'Classgate/student' in request.META.get('HTTP_REFERER') :
        messages.success(request,(" You've logged out successfuly! , be right back" ))
        return redirect('main')
    else:
        messages.success(request,(" You've logged out successfuly! , be right back" ))
        return redirect('main')




def edit(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_name = request.POST['new_name']
        user = authenticate(username=username,password=password)
        owner = request.user
        if user is not None  and request.user.username == username   and new_name != (''):
            owner.username = new_name
            owner.save()
            if 'Edit-user-AR/' in request.META.get('HTTP_REFERER') :
                messages.success(request,f'تم تغيير الاسم بنجاح {request.user.username}  استمتع !')
                return redirect('user-ar')
                
            elif 'Edit-user-EN/' in request.META.get('HTTP_REFERER') :
                messages.success(request,f'Nice name, username changed successfully into {request.user.username}')
                return redirect('userr')
    return render(request, 'index/edit.html',{
        'url': request.META.get('HTTP_REFERER'),
    })
    
    


def name_edit(request):
    return None


    

    
def name(request):
    return render(request,'index/edit.html',{
        
    })




def search(request):
    if request.method == 'POST':
        searchh = request.POST['q']
        alloutputs = ['login', 'membership', 'school',]
        recommend = []
        alloutputs_str = ", ".join(alloutputs)
        for output in alloutputs:
            if searchh == ('login') and request.user.username != (''):
                messages.error(request,' You are already logged in')
                return redirect('userr')
            elif searchh == ('login'):
                return redirect('log')
        
            elif searchh == ('membership') or searchh == ('school'):
                return redirect('code')
            if searchh.lower() in output.lower():
                recommend.append(output)
                messages.error(request,f'do you mean ? : {", ".join(recommend)}, These are all search categorys : {alloutputs_str} ')
                if request.user.username != (''):
                    return redirect('userr')
                else:
                    return redirect('main')

        else:
            
            messages.error(request,f'These are all search categorys : {alloutputs_str}')
            if request.user.username != (''):
               return redirect('userr')
            else:
                return redirect('main') 


    return render(request,'index/user.html')
def serv(request):
    return render(request,'index/user.html/')

def student(request):
    content = Content.objects.all()
    rule = Students.objects.get(name=request.session.get('my_name'))
    return render(request,'index/student.html',{
        'content':content,
        'rulee': rule
        
    })



def ex1(request,name,id):
    Examn = Exam.objects.get(id=id,name=name)
    ExamQuiz = ExamQ.objects.filter(examid=Examn)
    rule = Students.objects.get(name=request.session.get('my_name'))
    return render(request,'index/exam.html',{
        'url': 'eex',
      
        'exam': Examn,
        "examqs": ExamQuiz,
        'rulee': rule
    })









def e_Q(request,name ,id):
    Mark = 0
    rule = Students.objects.get(name=request.session.get('my_name'))
    my_name = request.session.get('my_name')
    Examn = Exam.objects.get(id=id,name=name)
    Quizes = ExamQ.objects.filter(examid=Examn)
    if request.method == 'POST':
        for quiz in Quizes:
           Q = request.POST[f'optionsfor{quiz.id}'] 
           if Q == quiz.answer:
                Mark += quiz.qmark

        exam_mark = ExamMark( school=rule.school, username=rule, exam_name=f'{Examn.category} : {Examn.name}', mark=Mark,fullmark=Examn.fullmark)
        exam_mark.save()                
        return render(request,'index/exam.html',{
        'mark':Mark,
        "exam":Examn,
        'rulee': rule
        
    })

usersall = User.objects.all()
    
def main_ar(request):
    Total = Students.objects.count()
    return render(request,'index/Taha-AR.html',{
     'usersss'  : User.objects.count(),
        'total':Total
    })

def user_ar(request):
    Total = Students.objects.count()
    return render(request,'index/user-AR.html',{
     'usersss'  : User.objects.count(),
        'total':Total
    })



def sch1_exams(request):
    Examn = Exam.objects.all()
    rule = Students.objects.get(name=request.session.get('my_name'))
    return render(request,'index/Sch1-exams.html',{
        'exams': Examn,
        "rulee": rule
    })


def Marks(request):
    my_name = request.session.get('my_name')
    
    rule = Students.objects.get(name=request.session.get('my_name'))
    tests = ExamMark.objects.filter(username=rule)
 
    return render(request,'index/marks.html',{
        'tests': tests,
        'rulee':rule
    })

def Addview(request):
    rule = Students.objects.get(name=request.session.get('my_name'))
 
    return render(request,'index/add.html',{
        'rulee':rule
    })
def Add(request):
  
  rule = Students.objects.get(name=request.session.get('my_name'))
 
  if request.method == 'POST':
      choice = request.POST['choice']
      return render(request,'index/add.html',{
        'rulee':rule,
        'choice':choice
    })
      
def AddExam(request):  
  rule = Students.objects.get(name=request.session.get('my_name'))
  if request.method == 'POST':
      cate = request.POST['category']
      name = request.POST['name']
      namear = request.POST['namear']
      qnum = request.POST['qnum']
      full = request.POST['fullmark']
      half = request.POST['half']
      exam_form = Exam(school=rule.school,arname=namear, teacher=rule,category=cate, name=name,quizsnumber=qnum,fullmark=full,half=half)
      exam_form.save()
      choice = 'exform'
      
      return render(request,'index/add.html',{
        'rulee':rule,
        'stformid':range(int(exam_form.quizsnumber)),
        'choice':choice,
        'ids':exam_form
    })
def Quizform(request):
    forqq = Exam.objects.get(id=request.POST['qfor'])
    if request.method == 'POST':
        x = 1
        for num in range(int(forqq.quizsnumber)):
            
            forq = Exam.objects.get(id=request.POST['qfor'])
            Q = request.POST[f'quiz-{num}']
            A = request.POST[f'answ-{num}']
            M = request.POST[f'mark-{num}']
            Op1 = x
            x +=1
            Op2 = x
            x +=1
            examQ_form = ExamQ(examid=forq, question=Q,answer=A,qmark=M,opt1id=Op1,opt2id=Op2)
            examQ_form.save()
    if '-ar' in request.build_absolute_uri():
        return redirect('add-ar')
    else:
        return redirect('add')
 

def AddVideo(request):  
  rule = Students.objects.get(name=request.session.get('my_name'))
  if request.method == 'POST':
      key = request.POST['keyword']
      title = request.POST['title']
      video = request.POST['video']
      link = request.POST['link']
      
      video_form = Content(school=rule.school, teacher=rule, keyword=key, title=title,vedio=video,link=link,)
      video_form.save()
      
      
      if '-ar' in request.build_absolute_uri():
          return redirect('add-ar')
      else:
          return redirect('add')