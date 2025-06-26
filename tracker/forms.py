from django import forms
from .models import ProblemRevision

class ProblemRevisionForm(forms.ModelForm):
    class Meta:
        model = ProblemRevision
        fields = ['problem', 'link', 'date','difficulty','notes', 'day_1', 'day_3', 'day_5', 'day_7']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
