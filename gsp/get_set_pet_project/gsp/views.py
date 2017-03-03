from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Just checking everything's tickety-boo"}
    return render(request, 'gsp/index.html', context=context_dict)

def about(request):
    return HttpResponse('This is the about page  <a href="/gsp/">Index</a>')
