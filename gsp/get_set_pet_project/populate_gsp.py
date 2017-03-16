import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'get_set_pet_project.settings')

import django
django.setup()
from gsp.models import Category, Page

def populate():

    
    cats = [{"title": "more cats",
             "url":"http://icanhas.cheezburger.com/lolcats"}]
    
    dogs = [{"title": "more dogs",
             "url":"about:blank"}]
    
    small_mammals = [{"title": "more smol mammals",
                      "url":"about:blank"}]
    
    birds = [{"title": "more birds",
             "url":"about:blank"}]

    fish = [{"title": "more fish",
             "url":"about:blank"}]

    reptiles = [{"title": "more reptiles",
                 "url":"about:blank"}]

    equine = [{"title": "more horses",
               "url":"about:blank"}]

    other = [{"title": "more dogs",
             "url":"about:blank"}]

    # Called it cates because categories takes too long to type and we have
    # a cats page already. Categories are referred to as cate or cates
    cates = {"Cats": {"pages": cats},
            "Dogs": {"pages": dogs},
            "Small Mammals": {"pages": small_mammals},
            "Birds": {"pages": birds},
            "Fish": {"pages": fish},
            "Reptiles": {"pages": reptiles},
            "Equine": {"pages": equine},
            "Other": {"pages": other} }

    for cate, cate_data in cates.iteritems():
        c = add_cate(cate)
        for p in cate_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cate, title, url, views=0):
    p = Page.objects.get_or_create(category=cate, title=title)[0]
    p.url=url
    p.save()
    return p

def add_cate(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Starts execution here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
