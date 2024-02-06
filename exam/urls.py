"""
URL configuration for exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path, include

from myapp import views
from student import views as myviews
from .import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from . import settings
from django.urls import path,include
from django.contrib import admin
from myapp import views

from django.contrib.auth.views import LogoutView,LoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    #on 9thdec
    path('student/', include('student.urls')),
    #on 18dec
    path('teacher/', include('teacher.urls')),
    #on 28dec
    #path('answer_evaluation/', include('answer_evaluation.urls')),
    #on 4thdec
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('admin-course', views.admin_course_view,name='admin-course'),
    path('admin-question', views.admin_question_view,name='admin-question'),
    path('admin-add-course', views.admin_add_course_view, name='admin-add-course'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    #on 5thdec
    path('admin-view-course', views.admin_view_course_view,name='admin-view-course'),
    #on 6thdec
    path('admin-view-question', views.admin_view_question_view,name='admin-view-question'),
    path('view-question/<int:pk>', views.view_question_view,name='view-question'),
    path('delete-question/<int:pk>', views.delete_question_view,name='delete-question'),
    path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),
    #on 8th dec
    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('admin-view-student-marks', views.admin_view_student_marks_view,name='admin-view-student-marks'),
    path('admin-view-marks/<int:pk>', views.admin_view_marks_view,name='admin-view-marks'),
    path('admin-check-marks/<int:pk>', views.admin_check_marks_view,name='admin-check-marks'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    #on 11dec
    #path('student-dashboard',myviews.student_dashboard,name='student-dashboard'),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='logout.html'),name='logout'),
    #on 14dec
    path('admin-view-teacher', views.admin_view_teacher_view, name='admin-view-teacher'),
    path('update-teacher/<int:pk>', views.update_teacher_view, name='update-teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher_view, name='delete-teacher'),
    #on 15dec
    #On 18dec
    path('admin-teacher', views.admin_teacher_view,name='admin-teacher'),
    path('admin-view-pending-teacher', views.admin_view_pending_teacher_view,name='admin-view-pending-teacher'),
    path('approve-teacher/<int:pk>', views.approve_teacher_view,name='approve-teacher'),
    path('reject-teacher/<int:pk>', views.reject_teacher_view,name='reject-teacher'),
    #on28dec
    #path('evaluateanswer', views.evaluate_answer,name='evaluateanswer'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
