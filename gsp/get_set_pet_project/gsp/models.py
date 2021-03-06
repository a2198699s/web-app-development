from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from star_ratings.models import Rating


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    img = models.CharField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Sets a file path so that it will go media/<username>/<filename>
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user, filename)


class Upload(models.Model):   
    # Not sure how necessary this is yet, hopefully will work in a similar way to
    # pages and categories
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=128)
    # uploads the file to path as defined earlier
    picture = models.ImageField(upload_to=user_directory_path)
    ratings = models.ForeignKey(Rating)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

#Upload.objects.filter(ratings__isnull=False).order_by('ratings__average')

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    #website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    #favourites = models.ForeignKey(Upload)
    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username
