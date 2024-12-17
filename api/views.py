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

def delete_products(request, id):
    try:
        instance = Product.objects.get(id=id)
        instance.delete()
        return redirect('home')
    except:
        return redirect('home')