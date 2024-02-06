from django.urls import path
from .views import evaluate_answer

app_name = 'answer_evaluation'

urlpatterns = [
    #path('evaluate/<int:question_id>/', evaluate_answer, name='evaluate_answer'),
    # Add more paths as needed for your application
]
