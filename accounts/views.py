from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate

user =get_user_model()
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        new_user = user.objects.create(username=username,password=password)
        login(request,new_user)
        return redirect('index')
    if not request.user.is_authenticated: 
        return render(request,'signup.html')
    else:
        return redirect('index')

def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password =request.POST.get("password")

        user = authenticate(username=username,password=password) 
        if user:
            login(request,user)
            return redirect('index')
    
    if request.method == "GET":
        if not request.user.is_authenticated: 
            return render(request,'login.html')
        else:
            return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('login')
