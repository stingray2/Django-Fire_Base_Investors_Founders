from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from founders.models import Profile
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'oops!!!!!! Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'oops!!!!!!Username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('/')

        else:
            messages.info(request,'oppss!!!! Password Not Maching ')
            return redirect('register')
    else:
        return render(request,'core/register.html')