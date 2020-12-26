from django.contrib import admin
from Userapp.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display=['user','country']
	list_filter=['user',]
admin.site.register(UserProfile,UserProfileAdmin)