from django import forms

from app.models import *

class studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    address=forms.CharField(max_length=100)

class bheemasenaMF(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
        







