import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'get_set_pet_project.settings')

import django
django.setup()
from gsp.models import Category # Page

def populate():

    placeholders = {"Maru":{"name": "maru", "picture": "maru.jpg", "cate":"Cats"},
                    "Maru": {"name": "maru", "picture": "maru.jpg", "cate": "Cats"},
                    "Maru": {"name": "maru", "picture": "maru.jpg", "cate": "Cats"},
                    "Maru": {"name": "maru", "picture": "maru.jpg", "cate": "Cats"},}

    # Called it cates because categories takes too long to type and we have
    # a cats page already. Categories are referred to as cate or cates
    cates = {"Cats":{"title": "Cats", "img": "maru.jpg"},
             "Dogs":{"title": "Dogs", "img": "dog4.jpg"},
             "Small Mammals":{"title": "Small Mammals", "img": "Herbert.jpg"},
             "Birds":{"title":"Birds", "img": "birb.jpg"},
            #"Fish": {"pages": fish},
             "Fish":{"title": "Fish", "img": "Mr Splashy-pants.jpg"},
            #"Reptiles": {"pages": reptiles},
             "Reptiles":{"title":"Reptiles", "img": "Polly.jpg"},
            #"Equine": {"pages": equine},
             "Equine":{"title": "Equine", "img": "Horace.jpg"},
            #"Other": {"pages": other}
             "Other":{"title": "Other", "img": "Ant and Dec.jpg"},  }

    for cate, cate_data in cates.iteritems():
        c = add_cate(cate_data["title"], cate_data["img"])
        #for p in cate_data["pages"]:
            #add_page(c, p["title"], p["img"])

    for upload, p_data in placeholders.iteritems():
        p = add_placeholder(p_data["name"], p_data["picture"], 0, admin, p_data["cate"])


def add_cate(name, image):
    c = Category.objects.get_or_create(name=name, img=image)[0]
    c.save()
    return c

def add_placeholder(name, picture, rating, user, category):
    p = Upload.objects.get_or_create(name=name,
                                     category=category,
                                     user=user,
                                     picture=picture,
                                     rating=rating)
    p.save()
    return p
# Starts execution here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
