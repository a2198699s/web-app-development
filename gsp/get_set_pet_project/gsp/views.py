from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from gsp.models import Category
from gsp.models import Page
from gsp.models import Upload
from gsp.forms import CategoryForm
from gsp.forms import PageForm
from gsp.forms import UserForm, UserProfileForm
from gsp.forms import UploadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def index(request):
    request.session.set_test_cookie()
    return render(request, 'gsp/index.html')


def about(request):
    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
        request.session.delete_test_cookie()
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
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
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


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'gsp/add_page.html', context_dict)


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

@login_required
# a lot of guesswork here I'll be honest
def user_upload(request):
    context_dict={}

    if request.method == 'POST':

        upload_form = UploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            print 'form is_valid'

            upload = upload_form.save(commit=False)
            upload.user = request.user
            upload.name = name

            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()

            return render(request, 'gsp/upload.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()

        context_dict = {'upload_form' : upload_form}
        all_categories = Category.objects.order_by('-id')
        context_dict['all_categories'] = all_categories
        print context_dict

    uploads = Upload.objects.all()

    return render(request, 'gsp/upload.html', context_dict)
