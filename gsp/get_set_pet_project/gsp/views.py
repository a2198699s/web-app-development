from django.shortcuts import render
from django.http import HttpResponse
from gsp.models import Category

def index(request):
	return render(request, 'gsp/index.html', context=context_dict)

def about(request):
	return HttpResponse('This is the about page  <a href="/gsp/">Index</a>')


def cats(request):
	category_list = Category.objects.order_by('-likes') 
	context_dict = {'categories': category_list}
	return render(request, 'gsp/cats.html', context=context_dict)
	
