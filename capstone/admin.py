from django.contrib import admin
from .models import user_contact

class user_contactAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','celphone','email','message',"timestamp")
    
admin.site.register(user_contact, user_contactAdmin)