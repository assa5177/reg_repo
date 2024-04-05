from django.shortcuts import render

from regapp.forms import Employeeform
# Create your views here.
def regview(request):
    if request.method=='POST':
       form=Employeeform(request.POST)
       if form.is_valid():
           form.save(commit=True)
    form=Employeeform()
    return render(request,'regapp/get.html',{'form':form})       