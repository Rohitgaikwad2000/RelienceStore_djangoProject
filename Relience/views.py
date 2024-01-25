from django.shortcuts import render, HttpResponse,redirect
import csv
from.models import Product
from.forms import csvuploadform

# Create your views here.

def handled_upload_csv(csv_file):
    decode_file = csv_file.read().decode('utf-8').splitlines()
    csv_reader = csv.reader(decode_file)
    headers = next(csv_reader)
    for row in csv_reader:
            employee_data = dict(zip(headers, row))
            # print("employee_data:-", employee_data)             # print all the data in terminal
            Product.objects.create(**employee_data)


def upload_csv(request):
    if request.method == "POST":
        form = csvuploadform(request.POST, request.FILES)
        if form.is_valid:
            handled_upload_csv(request.FILES["csv_file"])
            return HttpResponse("File uploaded succesfullyy.......")
    else:
        form = csvuploadform()
    return render(request, 'upload_csv.html', {"form":form})
    

        
def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {"products":products})


def add_product(request):
    if request.method == "GET":
        return render(request,'add_product.html')
    elif request.method == "POST":
        data = request.POST
        if not data.get("id"):
            Product.objects.create(name = data.get("name"), Brand = data.get("Brand"),
                                waranty = data.get("waranty"),price = data.get("price"))
        else:
            product = Product.objects.get(id = data.get("id"))
            product.name = data.get("name")
            product.Brand = data.get("Brand")
            product.waranty = data.get("waranty")
            product.price = data.get("price")
            product.save()
        return redirect("all_products")        



def update_product(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        return render(request, 'add_product.html', {"product":product})
    

def delete_product(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        product.is_available = True
        product.save()
    return redirect("all_products")        


def deleted_product(request):
    product = Product.objects.filter(is_available = True)
    return render(request, 'deleted_product.html', {"product":product})



def restore_product(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        product.is_available = False
        product.save()
    return redirect("all_products")    

        

def permanantly_delete(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        product.delete()
    return redirect("deleted_product")    
