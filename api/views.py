from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username', None).strip()
        password = request.POST.get('password', None).strip()
        if username == '' or password == '':
            messages.error(request, "username or password fields is requied")
            return redirect('signin')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username or password incorrect")
            return redirect('signin')
    return render(request, 'login.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def home(request):
    dicts = {
        "products":Product.objects.all()
    }
    return render(request, 'index.html',dicts)

@login_required(login_url='signin')
def add_products(request):
    if request.method == 'POST':
        image = request.FILES.get('image', None) 
        name = request.POST.get('name', None).strip()
        description = request.POST.get('description', None).strip()
        price = request.POST.get("price", None).strip()
        if name == "":
            messages.error(request, "name can't be blank")
            return redirect('add_products')
        if not image:
            messages.error(request, "Image can't be blank")
            return redirect('add_products')
        Product.objects.create(name = name, image = image, description = description, price = price)
        return redirect('home')
    return render(request,'add_products.html')

@login_required(login_url='signin')
def edit_product(request, id):
    if request.method == 'POST':
        image = request.FILES.get('image', None) 
        name = request.POST.get('name', None).strip()
        description = request.POST.get('description', None).strip()
        price = request.POST.get("price", None).strip()
        product_instance = Product.objects.filter(id=id).first()
        if name:
            product_instance.name = name
        if image:
            product_instance.image = image
        if description:
            product_instance.description = description
        if price:
            product_instance.price = price
        product_instance.save()
        return redirect('home')
    try:
        product_id = Product.objects.get(id=id)
    except:
        return redirect('home')
    return render(request,'edit_product.html',{'edit_data':product_id})

@login_required(login_url='signin')
def delete_products(request, id):
    try:
        instance = Product.objects.get(id=id)
        instance.delete()
        return redirect('home')
    except:
        return redirect('home')