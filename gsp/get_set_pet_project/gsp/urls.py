from django.conf.urls import url
from gsp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^cats/', views.cats, name='cats'),
    url(r'about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category,
        name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^upload/$', views.user_upload, name='upload'),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
]

# Handy Links

# <a href="/gsp/add_category/">Add a New Category</a><br /> Link to add_category
# <ul>
# <li><a href="{% url 'add_category' %}">Add a New Category</a></li>
# <li><a href="{% url 'about' %}">About</a></li>
# <li><a href="{% url 'index' %}">Index</a></li>
# <li><a href="{% url 'register' %}">Sign Up</a></li>
# <li><a href="{% url 'login' %}">Sign In</a></li>
# </ul>
