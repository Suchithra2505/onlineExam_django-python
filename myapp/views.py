
from . import forms,models
from .models import Course
#on 11dec
from . import forms,models
from student.models import Student
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from student import forms as SFORM
from django.conf import settings
from django.contrib.auth.models import Group
#on8thdec
from student import models as SMODEL
from student import forms as SFORM
from django.contrib.auth.models import User
#on 14dec
from teacher import models as TMODEL
from teacher import forms as TFORM
from django.db.models import Sum
# Create your views here.
def index(request):
    return render(request,"index.html")
#4thdec
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')
#on 18dec
def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

def afterlogin_view(request):
    if is_student(request.user):
        return redirect('student/student-dashboard')

    elif is_teacher(request.user):
        accountapproval = TMODEL.Teacher.objects.all().filter(user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('teacher/teacher-dashboard')
        else:
            return render(request, 'teacher_wait_for_approval.html')
    else:
        return redirect('admin-dashboard')
 #on 9th dec
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()
def admin_dashboard_view(request):

    return render(request,'admin_dashboard.html')
def admin_course_view(request):
    return render(request,'admin_course.html')
def admin_question_view(request):
    return render(request,'admin_question.html')
def admin_add_course_view(request):
    courseForm=forms.CourseForm()
    if request.method=='POST':
        courseForm=forms.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-course')
    return render(request,'admin_add_course.html',{'courseForm':courseForm})
def admin_add_question_view(request):
    questionForm=forms.QuestionForm()
    if request.method=='POST':
        questionForm=forms.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=models.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-question')
    return render(request,'admin_add_question.html',{'questionForm':questionForm})
#5th dec
def admin_view_course_view(request):
    courses = Course.objects.all()
    return render(request,'admin_view_course.html',{'courses':courses})
#6th dec
def admin_view_question_view(request):
    courses= models.Course.objects.all()
    return render(request,'admin_view_question.html',{'courses':courses})
def view_question_view(request,pk):
    questions=models.Question.objects.all().filter(course_id=pk)
    return render(request,'view_question.html',{'questions':questions})
def delete_question_view(request,pk):
    question=models.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/admin-view-question')
def delete_course_view(request,pk):
    course=models.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/admin-view-course')
#8th dec
def admin_student_view(request):
    dict={
    'total_student':SMODEL.Student.objects.all().count(),
    }
    return render(request,'admin_student.html',context=dict)
def admin_view_student_view(request):
    students= SMODEL.Student.objects.all()
    return render(request,'admin_view_student.html',{'students':students})
def admin_view_student_marks_view(request):
    students= SMODEL.Student.objects.all()
    return render(request,'admin_view_student_marks.html',{'students':students})
def admin_view_marks_view(request,pk):
    courses = models.Course.objects.all()
    response =  render(request,'admin_view_marks.html',{'courses':courses})
    response.set_cookie('student_id',str(pk))
    return response

def admin_check_marks_view(request, pk):
    course = models.Course.objects.get(id=pk)
    student_id = request.COOKIES.get('student_id')
    student = SMODEL.Student.objects.get(id=student_id)

    results = models.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request, 'admin_check_marks.html', {'results': results})
def update_student_view(request,pk):
    student=SMODEL.Student.objects.get(id=pk)
    user=SMODEL.User.objects.get(id=student.user_id)
    userForm=SFORM.StudentUserForm(instance=user)
    studentForm=SFORM.StudentForm(request.FILES,instance=student)
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=SFORM.StudentUserForm(request.POST,instance=user)
        studentForm=SFORM.StudentForm(request.POST,request.FILES,instance=student)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            studentForm.save()
            return redirect('admin-view-student')
    return render(request,'update_student.html',context=mydict)

def delete_student_view(request,pk):
    student=SMODEL.Student.objects.get(id=pk)
    user=User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return HttpResponseRedirect('/admin-view-student')

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'index.html')
#on 14dec

def admin_teacher_view(request):
    dict={
    'total_teacher':TMODEL.Teacher.objects.all().filter(status=True).count(),
    'pending_teacher':TMODEL.Teacher.objects.all().filter(status=False).count(),
    'salary':TMODEL.Teacher.objects.all().filter(status=True).aggregate(Sum('salary'))['salary__sum'],
    }
    return render(request,'admin_teacher.html',context=dict)


def admin_view_teacher_view(request):
    teachers= TMODEL.Teacher.objects.all().filter(status=True)
    return render(request,'admin_view_teacher.html',{'teachers':teachers})

def update_teacher_view(request,pk):
    teacher=TMODEL.Teacher.objects.get(id=pk)
    user=TMODEL.User.objects.get(id=teacher.user_id)
    userForm=TFORM.TeacherUserForm(instance=user)
    teacherForm=TFORM.TeacherForm(request.FILES,instance=teacher)
    mydict={'userForm':userForm,'teacherForm':teacherForm}
    if request.method=='POST':
        userForm=TFORM.TeacherUserForm(request.POST,instance=user)
        teacherForm=TFORM.TeacherForm(request.POST,request.FILES,instance=teacher)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacherForm.save()
            return redirect('admin-view-teacher')
    return render(request,'update_teacher.html',context=mydict)

def delete_teacher_view(request,pk):
    teacher=TMODEL.Teacher.objects.get(id=pk)
    user=User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return HttpResponseRedirect('/admin-view-teacher')
#on 18dec
def admin_view_pending_teacher_view(request):
    teachers= TMODEL.Teacher.objects.all().filter(status=False)
    return render(request,'admin_view_pending_teacher.html',{'teachers':teachers})

def approve_teacher_view(request,pk):
    teacherSalary=forms.TeacherSalaryForm()
    if request.method=='POST':
        teacherSalary=forms.TeacherSalaryForm(request.POST)
        if teacherSalary.is_valid():
            teacher=TMODEL.Teacher.objects.get(id=pk)
            teacher.salary=teacherSalary.cleaned_data['salary']
            teacher.status=True
            teacher.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-pending-teacher')
    return render(request,'salary_form.html',{'teacherSalary':teacherSalary})

def reject_teacher_view(request,pk):
    teacher=TMODEL.Teacher.objects.get(id=pk)
    user=User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return HttpResponseRedirect('/admin-view-pending-teacher')

def admin_view_teacher_salary_view(request):
    teachers= TMODEL.Teacher.objects.all().filter(status=True)
    return render(request,'admin_view_teacher_salary.html',{'teachers':teachers})

