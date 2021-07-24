from django.contrib.auth.models import User
from django.db.models import fields
from .models import UserPermission,UserAccount
from django import forms

class UserPermissionForm(forms.ModelForm):
    class Meta:
        model = UserPermission
        fields = ['type_of_permission','active']

class UserAccountForm(forms.ModelForm):
    permis = forms.ModelMultipleChoiceField(UserPermission.objects.all())
    class Meta:
        model = UserAccount
        fields = ['username','active','permis','image']
        

