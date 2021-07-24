from django import forms
from django.db.models.deletion import ProtectedError
from django.db.models.fields import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import MainGroup,PartGroups,ProductGroup,Products
from .forms import MainGroupForm,PartGroupForm,ProductGroupForm,ProductsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers

@login_required
def create_maingroup(request):
    lists = MainGroup.objects.all().order_by('-pk')
    form = MainGroupForm()
    if request.is_ajax() and request.method == 'POST':
        form = MainGroupForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.admin = request.user
            obj.save()
            messages.success(request,'زیادکرا')
            return JsonResponse({'success':'success'})
        else:
            return JsonResponse({'sucess':False,'error_msg':form.errors,'error_code':'invalid'})
    context = {
        'form':form,'lists':lists
    }
    return render(request,'products/create_maingroup.html',context)

@login_required
def list_maingroup(request):
    lists = MainGroup.objects.all().order_by('-pk')
    list_serializers = serializers.serialize('json',lists)
    return HttpResponse(list_serializers,content_type='application/json')

@login_required
def update_maingroup(request,id):
    lists = MainGroup.objects.all().order_by('-pk')
    object = get_object_or_404(MainGroup,id=id)
    form = MainGroupForm(instance=object)
    if request.method == 'POST':
        form = MainGroupForm(request.POST,instance=object)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'نوێکرایەوە')
            return redirect('products:maingroup')
    
    context = {
        'lists':lists,'form':form
    }
    return render(request,'products/update_maingroup.html',context)
                    
@login_required
def delete_maingroup(request,id):
    try:
        object = get_object_or_404(MainGroup,id=id)
        object.delete()
        messages.error(request,'سڕایەوە')
        return redirect('products:maingroup')
    except ProtectedError:
        messages.info(request,'ناتوانی ئەم ناوە بسڕیتەوە')
    return redirect('products:maingroup')


@login_required
def create_partgroup(request):
    lists = PartGroups.objects.all().order_by('-pk')
    form = PartGroupForm()
    if request.is_ajax() and request.method == 'POST':
        form = PartGroupForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.admin = request.user
            obj.save()
            messages.success(request,'زیادکرا')
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'error_msg':form.errors,'error_code':'invalid'})
    context = {
        'lists':lists,'form':form
    }
    return render(request,'products/create_partgroup.html',context)

@login_required
def update_partgroup(request,id):
    lists = PartGroups.objects.all().order_by('-pk')
    object = get_object_or_404(PartGroups,id=id)
    form = PartGroupForm(instance=object)
    if request.method == 'POST':
        form = PartGroupForm(request.POST,instance=object)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'نوێکرایەوە')
            return redirect('products:partgroup')
    context = {
        'lists':lists,'form':form
    }
    return render(request,'products/update_partgroup.html',context)


@login_required
def delete_partgroup(request,id):
    try:
        object = get_object_or_404(PartGroups,id=id)
        object.delete()
        messages.error(request,'سڕایەوە')
        return redirect('products:partgroup')
    except ProtectedError:
        messages.info(request,'ناتوانی ئەم ناوە بسڕیتەوە')
    return redirect('products:partgroup')


@login_required
def create_productgroup(request):
    lists = ProductGroup.objects.all().order_by('-pk')
    form = ProductGroupForm()
    if request.is_ajax() and request.method == 'POST':
        form = ProductGroupForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.admin = request.user
            obj.save()
            messages.success(request,'زیادکرا')
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'error_msg':form.errors,'error_code':'invalid'})
    context = {
        'lists':lists,'form':form
    }
    return render(request,'products/create_productgroup.html',context)

@login_required
def update_productgroup(request,id):
    lists = ProductGroup.objects.all().order_by('-pk')
    object = get_object_or_404(ProductGroup,id=id)
    form = ProductGroupForm(instance=object)
    if request.method == 'POST':
        form = ProductGroupForm(request.POST,instance=object)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'نوێکرایەوە')
            return redirect('products:productgroup')
    
    context = {
        'lists':lists,'form':form
    }
    return render(request,'products/create_productgroup.html',context)

@login_required
def create_product(request):
    lists = Products.objects.all().order_by('-pk')
    form = ProductsForm()
    if request.is_ajax() and request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.admin = request.user
            obj.save()
            messages.success(request,'زیادکرا')
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'error_msg':form.errors,'error_code':'invalid'})
    context = {
        'lists':lists,'form':form
    }
    return render(request,'products/create_product.html',context)

@login_required
def update_product(request,id):
    lists = Products.objects.all().order_by('-pk')
    object = get_object_or_404(Products,id=id)
    form = ProductsForm(instance=object)
    if request.method == 'POST':
        form = ProductsForm(request.POST,instance=object)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'نوێکرایەوە')
            return redirect('products:product')
    
    context = {'lists':lists,'form':form}
    return render(request,'products/create_product.html',context)

@login_required
def home(request):
    return render(request,'main.html')


@login_required
def load_maingroup(request):
    maingroup_id = request.GET.get('category')
    main_type = MainGroup.objects.get(id=maingroup_id)
    partgroups = PartGroups.objects.filter(main_type=maingroup_id).all()
    return render(request,'products/dropdown.html',{'partgroups':partgroups,'main_type':main_type})



