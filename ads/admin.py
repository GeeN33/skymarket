from django.contrib import admin

from ads.models import  Comment, Ad
# Register your models here.

admin.site.register(Ad)
admin.site.register(Comment)


