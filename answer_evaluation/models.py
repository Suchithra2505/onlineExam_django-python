from django.db import models

# Create your models here.
from django.db import models

# descriptive_evaluation/models.py
from django.db import models

class DescriptiveAnswer(models.Model):
    question = models.CharField(max_length=255)
    reference_answer = models.TextField()
    user_answer = models.TextField()
