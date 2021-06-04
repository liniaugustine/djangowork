from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(r):
 return HttpResponse('Good morning')
def new(req):
 return HttpResponse('hai lini')
def firstpg(request):
     return render(request, 'firstpg.html')
