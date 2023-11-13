from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Bank


# Create your views here.
def demo(request):
    obj = Bank.objects.all()
    return render(request, "index1.html", {'result': obj})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credential")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('index1.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')


            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
            return redirect('login')

        else:
            messages.info(request, "password not match")
            return redirect('register')
            return redirect('/')

    return render(request, "register.html")


def reg_form(request):
    if request.method == 'POST':
        username = request.POST['Name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['mail']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account_type = request.POST['account_type']
        materials_provide = request.POST['materials_provide']

        if User.objects.filter(username=username).exists():
            messages.info(request, "username already exist")
            return redirect('reg_form')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email already exist")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, dob=dob, age=age, gender=gender,
                                            phone_number=phone_number,
                                            email=email, address=address, district=district, branch=branch,
                                            account_type=account_type, materials_provide=materials_provide)
            user.save();
            messages.info(request, "application accepted")
        return redirect('/')
    return render(request, "reg_form.html")
