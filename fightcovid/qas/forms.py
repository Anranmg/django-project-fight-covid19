from django import forms
from qas.models import Answer, Question, Tag


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ["title", "content"]

    # Convert uploaded File object to a picture
    def save(self, commit=True) :
        instance = super(QuestionForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance