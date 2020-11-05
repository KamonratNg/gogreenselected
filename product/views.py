from django.shortcuts import render
from django.http import HttpResponse
from .models import AllProduct

def Home(request):
	#return HttpResponse ('<h2>Hello GOGREEN</h2>')
	return render(request,'product/home.html')

def About(request):
	return render(request,'product/about.html')

def Pot(request):
	return render(request,'product/pot.html')	

def Plant(request):
	allproduct = AllProduct.objects.all()
	context = {'allproduct' : allproduct}
	return render(request,'product/plant.html',context)

def Ball(request):
	return render(request,'product/ball.html')	