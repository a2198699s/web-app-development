import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'get_set_pet_project.settings')

import django
django.setup()
from gsp.models import Category, Upload, UserProfile, User

def populate():


    # Called it cates because categories takes too long to type and we have
    # a cats page already. Categories are referred to as cate or cates
    cates = {"Cats":{"title": "Cats", "img": "maru.jpg"},
             "Dogs":{"title": "Dogs", "img": "dog4.jpg"},
             "Small Mammals":{"title": "Small Mammals", "img": "Herbert.jpg"},
             "Birds":{"title":"Birds", "img": "birb.jpg"},
             "Fish":{"title": "Fish", "img": "Mr Splashy-pants.jpg"},
             "Reptiles":{"title":"Reptiles", "img": "Polly.jpg"},
             "Equine":{"title": "Equine", "img": "Horace.jpg"},
             "Other":{"title": "Other", "img": "Ant and Dec.jpg"},  }

    for cate, cate_data in cates.iteritems():
		c = add_cate(cate_data["title"], cate_data["img"])


def add_cate(name, image):
    c = Category.objects.get_or_create(name=name, img=image)[0]
    c.save()
    return c

# Starts execution here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
