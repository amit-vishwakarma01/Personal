from django.contrib import admin
from .models import userlogin,company_detail,profile,todolist
# Register your models here.
admin.site.register(userlogin)
admin.site.register(company_detail)
admin.site.register(profile)
admin.site.register(todolist)