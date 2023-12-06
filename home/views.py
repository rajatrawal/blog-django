from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from blog.models import Blog
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
# Create your views here.


def index(request):
    blogs = Blog.objects.all()
    params = {"text": "Blogs", "blogs": blogs}
    return render(request, "home/index.html", params)


def about(request):
    return render(request, "home/about.html")


def handel_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password2")
        user = authenticate(username=email, password=password)
        print(email, password, user)
        if user is not None:
            login(request, user)
            messages.success(request, "Loged in  Succesfully")
        else:
            messages.error(request, "Please Enter Valid Info Try Again")

        return redirect("index")
    else:
        return HttpResponse("Not Allowed")


def handel_logout(request):

    logout(request)
    messages.success(request, "Loged Out  Succesfully")
    return redirect("index")


def search(request):
    if request.method == "POST":
        txt = request.POST["search"]
        blogs = []
        for blog in Blog.objects.all():
            if(txt in blog.title+blog.content+blog.author):
                blogs.append(blog)
        if len(blogs) > 0:
            params = {"text": "Blogs", "blogs": blogs}
        else:
            blogs = Blog.objects.all()
            params = {
                "text": "No Results Found You can also Like", "blogs": blogs}
            messages.warning(request, 'No Results Found ')

    return render(request, "blog/index.html", params)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        text = request.POST.get("text")
        if len(name) > 4 and len(email) > 6 and len(phone) > 9 and len(text) > 2:
            contact = Contact(name=name, phone=phone, email=email, decs=text)
            contact.save()
            messages.info(request, 'Message has been sent')
        else:
            messages.error(request, 'Please Enter Valid Information ')
    return render(request, "home/contact.html")


def handel_sign_up(request):
    if request.method == "POST":
        try:
            name = request.POST["name"]
            print(name)
            email = request.POST["email2"]
            print(email)
            phonenumber = request.POST["phoneNumber"]
            print(phonenumber)
            password = request.POST["password1"]
            print(password)
            password2 = request.POST["password3"]
            print(password2)
            check = request.POST.get("check", "off")
            print(check)
            print(name,email,phonenumber,password,password2,check)
            if 10 <= len(phonenumber) < 14 and password == password2 and check == "on" and not name.isalnum():
                myuser = User.objects.create_user(email, email, password)
                myuser.first_name = name.split(" ")[0]
                myuser.last_name = name.split(" ")[-1]
                myuser.save()
                messages.success(request, "Account Created Succesfully")
            else:
                messages.error(request, "Enter valid info")
        except IntegrityError:
            messages.error(request, "Chose Another User Already Exist")
        except:
            
            messages.error(request, "An Error occoured")
        return redirect("index")
    else:
        return HttpResponse("Not Allowed")
