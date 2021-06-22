from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reg(req):
 return HttpResponse('Welcome To My Page')
def logintodo(request):
 return render(request,'logintodo.html')
def hometodo(request):
 return render(request,'hometodo.html')
def craccount(request):
 return render(request,'craccount.html')
 