from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def lamar(request):
    return render(request,'lamar.html')
def prank(request):
    return render(request,'prank.html')
def narasi(request):
    return render(request,'narasi.html')