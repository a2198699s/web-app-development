import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'get_set_pet_project.settings')

import django
django.setup()
from gsp.models import Category, Page

def populate():

    
    cats = [{"title": "Cats",
             "img":"maru.jpg"}]
    
    dogs = [{"title": "Dogs",
             "img":"dog4.jpg"}]
    
    small_mammals = [{"title": "Smol mammals",
                      "img":"Herbert.jpg"}]
    
    birds = [{"title": "Birds",
             "img":"birb.jpg"}]

    fish = [{"title": "Fish",
             "img":"Mr Splashy-pants.jpg"}]

    reptiles = [{"title": "Reptiles",
                 "img":"Polly.jpg"}]

    equine = [{"title": "Equine",
               "img":"baldrick.jpg"}]

    other = [{"title": "Other",
             "img":"Ant and Dec.jpg"}]

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
            add_page(c, p["title"], p["img"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cate, title, img, views=0):
    p = Page.objects.get_or_create(category=cate, title=title)[0]
    p.img=img
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
