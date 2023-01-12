from django.shortcuts import render
from . models import Invester
# Create your views here.
def home(request):
    return render(request,'core/home.html')

def investor(request):
    inv = Invester.objects.all()
    context ={
        'investor':inv
        }
    return render(request,'core/investor.html',context)