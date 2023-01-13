from django.shortcuts import render

# Create your views here.

def register_founder(request):
    return render(request,'core/register_with_founder.html')