from django import forms
from regapp.models import Employee

class Employeeform(forms.ModelForm):
    EName=forms.CharField()
    Enumber=forms.IntegerField()
    EAddress=forms.CharField()
    Esal=forms.FloatField()

    class Meta:
        model=Employee
        fields='__all__'