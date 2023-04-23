from django import forms
from .models import Course, User, Rating

class SearchForm(forms.Form):
    #query = forms.Charfield
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    gender = forms.MultipleChoiceField(choices=[('male', 'Male'), ('female', 'Female')], widget=forms.CheckboxSelectMultiple, required=False)
    


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']
    