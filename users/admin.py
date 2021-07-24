from django.contrib import admin
from .models import UserAccount,UserPermission

admin.site.register(UserAccount)

admin.site.register(UserPermission)
