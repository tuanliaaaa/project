from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request,'home/index.html')
def about(request):
    return render(request,'home/about.html')
def watches(request):
    return render(request,'home/watches.html')
def card(request):
    return render(request,'home/card.html')
def singerProduct(request):
    return render(request,'home/singerProduct.html')
def search(request):
    return render(request,'home/search.html')
