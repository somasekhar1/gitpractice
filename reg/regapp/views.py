from django.shortcuts import render
from .models import Register
# Create your views here.
def register(request):
    # return render(request,"registration.html")
# def registerdetails(request):
    if request.method=="POST":
        username=request.POST.get('username')
        print(username)
        email=request.POST.get('email')
        print(email)
        password=request.POST.get('password')
        print(password)
        Register(username=username,email=email,password=password).save()
    return render(request,"registration.html")