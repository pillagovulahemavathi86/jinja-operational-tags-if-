from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    d={'a':10}
    return render(request,'ifcondition.html',d)

