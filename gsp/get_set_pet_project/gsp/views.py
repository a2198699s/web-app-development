from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from gsp.models import Category
from gsp.models import Upload
from gsp.forms import CategoryForm
#from gsp.forms import PageForm
from gsp.forms import UserForm, UserProfileForm
from gsp.forms import UploadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def index(request):
    #request.session.set_test_cookie()
    return render(request, 'gsp/index.html')
	
def favourites(request):
    #request.session.set_test_cookie()
    return render(request, 'gsp/favourites.html')	


def about(request):
    #if request.session.test_cookie_worked():
        #print("TEST COOKIE WORKED!")
        #request.session.delete_test_cookie()
    return HttpResponse('This is the about page  <a href="/gsp/">Index</a>')


	
def cats(request):
    #category_list = Category.objects.order_by('-likes')
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'gsp/cats.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        #pages = Page.objects.filter(category=category)
        #context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        #context_dict['pages'] = None
    return render(request, 'gsp/category.html', context_dict)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'gsp/add_category.html', {'form': form})



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'gsp/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your GSP account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'gsp/login.html', {})


def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_upload(request):
    if request.method == 'POST':

        upload_form = UploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            
            upload = upload_form.save(commit=False)
            upload.user = request.user
            #upload.name = name
            #upload.category = category

            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()

            return render(request, 'gsp/upload.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
        #all_categories = Category.objects.order_by('-id')
    uploads = Upload.objects.all()

    return render(request, 'gsp/upload.html',
                  {'uploads': uploads, 'upload_form': upload_form})

def uploads(request):
    uploads = Upload.objects.all()
    
    return render(request, 'gsp/user_submitted.html',
                  {'uploads':uploads})

def top_rated(request):
    uploads = Upload.objects.filter(ratings__isnull=False).order_by('ratings__average')
    return render(request, 'gsp/top_rated.html', {'uploads': uploads})