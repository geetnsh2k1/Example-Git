from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from home.models import Response, Product, Like

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handlelogout(request):
    if request.method == "POST":
        logout(request)
    else:
        pass
    return redirect('home')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            print('user is present')
            login(request, user)
        else:
            print('no user found.')
    else:
        pass
    return redirect('home')

def handlesignup(request):
    if request.method == "POST":
        try:
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm = request.POST['confirm']

            print(fname, lname, username, password, confirm)

            user = authenticate(request, username=username, password=password)
            if user:
                print('user already exixts.')
            else:
                print('user can be created.')
                newuser = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
                newuser.save()
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('home')

def handleresponse(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            description = request.POST['description']
            phone = request.POST['phone']

            print(username, description, phone)

            user = User.objects.get(username=username)
            newresp = Response.objects.create(user=user, description=description, contact=phone)
            newresp.save()
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('home')

def viewproducts(request):
    products = Product.objects.all()
    return render(request, 'viewall.html', {'products':products})

def addproduct(request):
    print(request)
    return render(request, 'addproduct.html')

def handleaddproduct(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            price = request.POST['price']
            category = request.POST['category']
            description = request.POST['description']

            product = Product.objects.filter(name=name, category=category)
            if len(product) == 0:
                product = Product.objects.create(name=name, price=price, category=category, description=description)
                product.save()
                like = Like.objects.create(product=product)
                like.save()
            else:
                print("product can't added as it already exists.")
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('home')

def deletepage(request):
    products = Product.objects.all()
    return render(request, 'delete.html', {'products':products})

def handledeleteproduct(request):
    if request.method == "POST":
        pname = request.POST['pname']
        try:
            product = Product.objects.get(name=pname)
            product.delete()
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('home')

def handlelikes(request):
    try:
        if request.method == "POST":
            pname = request.POST['pname']
            like = request.POST['like']
            
            username = request.user.username
            product = Product.objects.get(name=pname)
            user = User.objects.get(username=username)

            if like == "Likes":
                like = Like.objects.get(product=product)
                like.user.add(user)
                like.count += 1
                like.save()
            else:
                print('unlike')
                like = Like.objects.get(product=product, user=user)
                like.user.remove(user)
                like.count -= 1
                like.save()
        else:
            pass
    except Exception as e:
        print(e)
    return redirect('allproducts')