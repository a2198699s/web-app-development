from django.contrib import admin
from gsp.models import Category #, Page
from gsp.models import UserProfile


#class PageAdmin(admin.ModelAdmin):
 #   list_display = ('title', 'category', 'img')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
#admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
