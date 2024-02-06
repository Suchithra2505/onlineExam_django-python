from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from . import forms,models
from django.conf import settings
from myapp import models as QMODEL
#on11dec
from django.contrib.auth.models import Group
#on 12dec
from datetime import date
from datetime import datetime, timedelta
from .models import Student



# Create your views here.
#def studentclick_view(request):
    #if request.user.is_authenticated:
        #return render(request,'studentlogin.html')
    #return render(request,'studentclick.html')
#def student_dashboard(request):
    #if request.user.is_authenticated:
        #return render(request,'student_dashboard.html')
#on 11dec
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'studentclick.html')

#on 9thdec
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'studentsignup.html',context=mydict)


def student_dashboard_view(request):
    dict = {

        'total_course': QMODEL.Course.objects.all().count(),
        'total_question': QMODEL.Question.objects.all().count(),
        'student':Student.objects.get(user_id=request.user.id)

    }

    return render(request, 'student_dashboard.html', context=dict)
#on 12thdec
def student_exam_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student_exam.html',{'courses':courses})


def take_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    total_questions = QMODEL.Question.objects.all().filter(course=course).count()
    questions = QMODEL.Question.objects.all().filter(course=course)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks

    return render(request, 'take_exam.html',
                  {'course': course, 'total_questions': total_questions, 'total_marks': total_marks})

def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    questions=QMODEL.Question.objects.all().filter(course=course)
    if request.method=='POST':
        pass
    response= render(request,'start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response
#on 13dec

def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = QMODEL.Course.objects.get(id=course_id)

        total_marks = 0
        questions = QMODEL.Question.objects.all().filter(course=course)
        for i in range(len(questions)):

            selected_ans = request.COOKIES.get(str(i + 1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = models.Student.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks = total_marks
        result.exam = course
        result.student = student
        result.save()

        return HttpResponseRedirect('view-result')

def view_result_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'view_rersult.html',{'courses':courses})

def check_marks_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'check_marks.html',{'results':results})


def student_marks_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'student_marks.html', {'courses': courses})
