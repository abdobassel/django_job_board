from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,authenticate
from .models import *
from django.urls import reverse


def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    context = {"form":form}

    return render(request, 'registration/signup.html',context)



def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}

    return render(request, 'accounts/profile.html', context)
    
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html',{'userform':userform,'profileform':profileform})