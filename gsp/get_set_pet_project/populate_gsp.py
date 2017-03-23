import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'get_set_pet_project.settings')

import django
django.setup()
from gsp.models import Category, Upload, UserProfile, User

def populate():

    placeholders = {"Upload1":{"name": "Ant and Dec", "picture": "AntAndDec.jpg", "cate":"Other"},
                "Upload2": {"name": "Baldrick", "picture": "baldrick.jpg", "cate": "Equine"},
                "Upload3": {"name": "Birb", "picture": "birb.jpg", "cate": "Birds"},
                "Upload4": {"name": "Dugg", "picture": "Dugg.jpg", "cate": "Dogs"},
                "Upload5": {"name": "Blep", "picture": "blep.jpg", "cate": "Dogs"},
                "Upload6": {"name": "Bubbles", "picture": "bubbles.jpg", "cate": "Fish"},
                "Upload7": {"name": "Butthead", "picture": "butthead.jpg", "cate": "Small Mammals"},
                "Upload8": {"name": "Chubs", "picture": "chubs.jpg", "cate": "Cats"},
                "Upload9": {"name": "Poe", "picture": "dogbutt.jpg", "cate": "Dogs"},
                "Upload10": {"name": "Peter", "picture": "giantrabbit.jpg", "cate": "Small Mammals"},
                "Upload11": {"name": "Herbert", "picture": "Herbert.jpg", "cate": "small Mammals"},
                "Upload12": {"name": "Mickey", "picture": "hey.jpg", "cate": "small Mammals"},
                "Upload13": {"name": "Horace", "picture": "Horace.jpg", "cate": "Equine"},
                "Upload14": {"name": "Dolly", "picture": "jumping_lamb.jpg", "cate": "Small Mammals"},
                "Upload15": {"name": "Maru", "picture": "maru.jpg", "cate": "Cats"},
                "Upload16": {"name": "Magikarp", "picture": "MrSplash.jpg", "cate": "Fish"},
                "Upload17": {"name": "Lilly", "picture": "Lilly.jpg", "cate": "Cats"},
                "Upload19": {"name": "Polly", "picture": "Polly.jpg", "cate": "Reptiles"},
                "Upload20": {"name": "Rocky", "picture": "Rocky.jpg", "cate": "Other"},
                #"Upload21": {"name": "Polly", "picture": "Polly.jpg", "cate": "Reptiles", "user": "admin"},
                #"Upload22": {"name": "Polly", "picture": "Polly.jpg", "cate": "Reptiles", "user": "admin"},
                #"Upload23": {"name": "Polly", "picture": "Polly.jpg", "cate": "Reptiles", "user": "admin"},
                #"Upload24": {"name": "Polly", "picture": "Polly.jpg", "cate": "Reptiles", "user": "admin"},
                #"Upload25": {"name": "Polly", "picture": "Polly.jpg", "cate": "Reptiles", "user": "admin"},
                #"Upload26": {"name": "Polly", "picture": "Polly.jpg", "cate": "Reptiles", "user": "admin"},
					}

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
		for upload, p_data in placeholders.iteritems():
		    if p_data["cate"] == cate_data["title"]:
			p = add_upload(p_data["name"], p_data["picture"], c)
        #for p in cate_data["pages"]:
            #add_page(c, p["title"], p["img"])

    #for upload, p_data in placeholders.iteritems():
        #p = add_placeholder(p_data["name"], p_data["picture"], p_data["rating"], p_data["user"], p_data["cate"])


def add_cate(name, image):
    c = Category.objects.get_or_create(name=name, img=image)[0]
    c.save()
    return c

def add_upload(name, picture, category):
    p = Upload.objects.get_or_create(name=name,
                                     category=category,
                                     picture=picture,)
    p.save()
    return p

def add_user(user):
	u = User.objects.get_or_create(id=user)
	u.save()
	return u
# Starts execution here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
