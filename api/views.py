from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages

# Create your views here.
def home(request):
    dicts = {
        "products":Product.objects.all()
    }
    
    return render(request, 'index.html',dicts)

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

def edit_product(request):
    return render(request,'edit_product.html')