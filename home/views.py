from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

def learn_more(request):
    return render(request, 'learn_more.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Logout Successfully...")
    return redirect('login')


def landingpage(request):
    return render(request, 'landingpage.html')

