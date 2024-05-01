from django.shortcuts import render, redirect
from .models import ProductMst, ProductSubCat
import os
from django.http import Http404

def index(request):
    if request.method == 'POST':
        data = request.POST
        product_name = data.get('product')
        price = data.get('price')
        image = request.FILES.get('img')
        model = data.get('model')
        ram = data.get('ram')

        
        product_instance = ProductMst.objects.filter(product_name=product_name).first()
        if product_instance:
            ProductSubCat.objects.create(product=product_instance,product_price=price,product_image=image,product_model=model,product_ram=ram)
            return redirect('/')
        else:
            return render(request, 'index.html', {'error': 'Product not found'})

    product = ProductMst.objects.all()
    subproduct = ProductSubCat.objects.all()
    return render(request, 'index.html', {'product': product, 'productsub': subproduct})

def delete(request, id):
        edata = ProductSubCat.objects.get(id=id)
        edata.delete()
        os.remove(edata.product_image.path)
        return redirect('/')

def edit(request, id):
    edata = ProductSubCat.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        product_name = data.get('product')
        product_instance = ProductMst.objects.filter(product_name=product_name).first()

        if product_instance:
            edata.product = product_instance
            edata.product_price = data.get('price')
            edata.product_model = data.get('model')
            edata.product_ram = data.get('ram')

            if request.FILES.get("img") is not None:
                os.remove(edata.product_image.path)
                edata.product_image = request.FILES.get("img")

            edata.save()
            return redirect('/')
        else:
            # Handle the case where the product instance is not found
            return render(request, 'update.html', {'error': 'Product not found'})

    product = ProductMst.objects.all()
    return render(request, 'update.html', {"edata": edata, 'product': product})
