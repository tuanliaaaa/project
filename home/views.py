from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Product,Transaction
from django.urls import reverse
def index(request):
    list_watch = Product.objects.all()[0:15]
    for i in list_watch:
        a = i.img.split(',')
        i.imgs = a
    return render(request,'home/index.html',{'list_watch':list_watch})
def watches(request):
    if request.GET:
        search = request.GET['search'][0:15]
        list_watch = Product.objects.filter(ProductCode__contains=search)|Product.objects.filter(ProductName__contains=search)
        print(type(list_watch))
        for i in list_watch:
            a = i.img.split(',')
            i.imgs = a
        return render(request,'home/watches.html',{'list_watch':list_watch})
    else:
        list_watch = Product.objects.all()
        for i in list_watch:
            a = i.img.split(',')
            i.imgs = a
        return render(request,'home/watches.html',{'list_watch':list_watch})
def card(request):
    List_Transaction = Transaction.objects.order_by("-dateBuy").all()[0:5]
    for i in List_Transaction:
        a = i.Product.img.split(',')
        i.Product.imgs = a
        
    return render(request,'home/card.html',{'List_Transaction':List_Transaction})
def singerProduct(request,id):
    ok=True
    list_singerProduct = Product.objects.get(pk=id)
    a = list_singerProduct.img.split(',')
    if request.POST:    
        quantily = request.POST['quantily']
        User = request.POST['User']
        if list_singerProduct.stock < int(quantily):
            ok = False     
            return render(request,'home/singerProduct.html',{'singerProduct':list_singerProduct,'ims':a,'ok':ok})
        else:
            b = Transaction(Product=list_singerProduct,quatily=quantily,UserName=User)
            b.save()
            list_singerProduct.stock-=int(quantily)
            list_singerProduct.save()
            return HttpResponseRedirect(reverse('card',))
    else:
        return render(request,'home/singerProduct.html',{'singerProduct':list_singerProduct,'ims':a,'ok':ok})

def showAll(request):
    list_watch = Product.objects.all()
    for i in list_watch:
        a = i.img.split(',')
        i.imgs = a
    return render(request,'home/watches.html',{'list_watch':list_watch})