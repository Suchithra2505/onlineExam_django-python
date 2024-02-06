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
from django.urls import path
from.import views
from django.contrib.auth.views import LoginView
from myapp import views as myappviews

urlpatterns = [
    #path('admin/', admin.site.urls),
    #on 30nov
   # path('index/', views.index),
    #on 9th dec
    path('studentclick', views.studentclick_view),
    #on 11dec
    path('afterlogin', myappviews.afterlogin_view,name='afterlogin'),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('studentlogin', LoginView.as_view(template_name='studentlogin.html'),name='studentlogin'),
    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    #on 12dec
    path('student-exam', views.student_exam_view,name='student-exam'),
    path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
    #on 13dec
    path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
    path('view-result', views.view_result_view,name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
    path('student-marks', views.student_marks_view,name='student-marks'),
]
