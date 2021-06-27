# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import PasswordChangeForm
# from . models import Crinfo,ReferralCode
from django.contrib.auth import update_session_auth_hash
# from cr_portal.models import  Points

def signup(request):

    if request.method=='POST':

        
        name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if name=="" or  username=='' or email=='' or password1 ==''or password2=="":
            messages.info(request,"fill all the details to sign up")
            return redirect("signup")
        elif not email.endswith("@gmail.com"):
            messages.info(request,"invalid gmail")
            return redirect("signup")
        
        else:
            if password1==password2:


                if User.objects.filter(username=username).exists():

                    messages.info(request,"user already exists")
                    return redirect('/accounts/signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email already exists")
                    return redirect('signup')

                else:

                    user=User.objects.create_user(first_name=name,email=email,username=username,password=password1)
                    user.save();
                    messages.info(request,"user created")
                    return redirect('login')
                   

            else:

                messages.info(request,"password not matching..")

                return redirect('signup')

    else:

        return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            authenticated = {
            "bool" : "True"
        }
            return render(request,'index.html',authenticated)
        else:
            messages.info(request,'authentication failed')
            return redirect('login')
    else:
        return render(request,'login.html')