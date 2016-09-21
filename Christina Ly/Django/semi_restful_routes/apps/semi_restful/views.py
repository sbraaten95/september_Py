from django.shortcuts import render, redirect
from .models import Product
from django.core.urlresolvers import reverse

def index(request):
	context = {
		'products':Product.objects.all()
	}
	return render(request, 'semi_restful/index.html', context)
def create(request):
	return render(request, 'semi_restful/create.html')
def process(request):
	products = Product(name = request.POST['name'], description = request.POST['description'], price=request.POST['price'])
	products.save()
	return redirect(reverse('semi_restful:my_products'))
def destroy(request,id):
	Product.objects.filter(id=id).delete()
	return redirect(reverse('semi_restful:my_products'))
def show(request,id):
	context = {
	'product': Product.objects.get(id=id)
	}
	return render(request, 'semi_restful/show.html', context)
def edit(request,id):
	context = {
	'product': Product.objects.get(id=id)
	}
	return render(request, 'semi_restful/edit.html', context)
def update(request,id):
	products = Product.objects.get(id=id)
	products.name = request.POST['name']
	products.description = request.POST['description']
	products.price = request.POST['price']
	products.save()
	return redirect(reverse('semi_restful:my_products'))


