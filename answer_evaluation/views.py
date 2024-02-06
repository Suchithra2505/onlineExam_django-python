from django.shortcuts import render

# Create your views here.
# descriptive_evaluation/views.py
from django.shortcuts import render
from django.views import View
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import DescriptiveAnswer

class EvaluateAnswersView(View):
    template_name = 'evaluate_answers.html'

    def get(self, request):
        # Fetch descriptive answers from the database
        answers = DescriptiveAnswer.objects.all()

        # Calculate cosine similarity
        for answer in answers:
            vectorizer = CountVectorizer().fit_transform([answer.reference_answer, answer.user_answer])
            similarity_matrix = cosine_similarity(vectorizer)
            answer.similarity_score = similarity_matrix[0, 1]

        context = {'answers': answers}
        return render(request, self.template_name, context)


