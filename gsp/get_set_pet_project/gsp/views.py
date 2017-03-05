from django.shortcuts import render
from django.http import HttpResponse
from gsp.models import Category
from gsp.models import Page


def index(request):
	return render(request, 'gsp/index.html')

def about(request):
	return HttpResponse('This is the about page  <a href="/gsp/">Index</a>')


def cats(request):
	category_list = Category.objects.order_by('-likes') 
	context_dict = {'categories': category_list}
	return render(request, 'gsp/cats.html', context=context_dict)
	
def show_category(request, category_name_slug): 
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages 
		context_dict['category'] = category 
	except Category.DoesNotExist: 
		context_dict['category'] = None 
		context_dict['pages'] = None
	return render(request, 'rango/category.html', context_dict)