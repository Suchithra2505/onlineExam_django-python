from django import forms

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)