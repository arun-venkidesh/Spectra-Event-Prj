from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from spectraeventapp.forms import RegisterForm,EventRegistrationForm

# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        Email= request.POST['Email']
        Password= request.POST['Password']
        user= authenticate(request, Email=Email, Password=Password)
        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request,'login.html')


def booking(request):
    if request.method=="POST":
        print("done")
        form=EventRegistrationForm(request.POST)
        print("save")
        if form.is_valid():
            form.save()
            return redirect('/')
            print("sucess")
    else:
        form=EventRegistrationForm()
    return render(request,'eventbooking.html',{'form':form})

def main(request):
    return render(request,'main.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contactus.html')