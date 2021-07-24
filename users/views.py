from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import auth
from django.utils.translation import gettext_lazy as _

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(reverse_lazy('products:maingroup'))
        messages.error(request,_('تکایە دڵنیابەرەوە لە راستی زانیاریەکانت!'))
        return redirect(reverse_lazy('login'))
    else:
        return render(request,'login.html')
