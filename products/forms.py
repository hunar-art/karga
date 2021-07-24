from django.db.models import fields
from django.forms import widgets
from .models import Products,ProductGroup,PartGroups,MainGroup
from django import forms
from django.utils.translation import gettext_lazy as _

class MainGroupForm(forms.ModelForm):
    class Meta:
        model = MainGroup
        fields = ['main_type']

        error_messages = {
            'main_type':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
                'unique':_('تکایە ئەم زانیاریە داغڵکراوە'),

            }
        }
        widgets = {
            'main_type':forms.TextInput(attrs={'class':'form-control','placeholder':_('زیادکردنی ناوی گروپی سەرەکی')})
        }


class PartGroupForm(forms.ModelForm):
    main_type = forms.ModelChoiceField(queryset=MainGroup.objects.all(),empty_label=_('هەڵبژاردنی کاڵای سەرەکی'))
    class Meta:
        model = PartGroups
        fields = ['main_type','part_group']

        error_messages = {
            'main_type':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
            },
            'part_group':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
            }

        }
        widgets = {
            'part_group':forms.TextInput(attrs={'placeholder':_('ناوی گروپی فرعی')})
        }


class ProductGroupForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        fields = ['product_group']

        error_messages = {
            'product_group':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
                'unique':_('تکایە ئەم زانیاریە داغڵکراوە'),

            }
        }
        widgets = {
            'product_group':forms.TextInput(attrs={'placeholder':_('ناوی گروپی کاڵا')})
        }

class ProductsForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=MainGroup.objects.all(),empty_label=_('هەڵبژاردنی ناوی گروپی ئەسڵی'))
    part_group = forms.ModelChoiceField(queryset=PartGroups.objects.all(),empty_label='هەڵبژاردنی ناوی گروپی فەرعی')
    product_group = forms.ModelChoiceField(queryset=ProductGroup.objects.all(),empty_label=_('هەڵبژاردنی ناوی گروپی کاڵا'))
    class Meta:
        model = Products
        fields = [
            'category','part_group','product_group','product_name','qnt_in_box','kg_single',
            'kg_box','info_1','info_2','info_3'
            ]

        error_messages = {
            'category':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
            },
            'part_group':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
            },            
            'product_group':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
            },
            'product_name':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
                'unique':_('تکایە ئەم زانیاریە داغڵکراوە'),
            },
            'qnt_in_box':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
            },            
            'kg_box':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
            },
            'kg_single':{
                'required':_('تکایە ناتوانی ئەم بەشە بە بەتاڵی بەجێ بهێڵیت'),
            },

        }
        widgets = {
            'product_name':forms.TextInput(attrs={'placeholder':_('ناوی کاڵا')}),
            'info_1':forms.TextInput(attrs={'placeholder':_('زانیاری زیادە ١')}),
            'info_2':forms.TextInput(attrs={'placeholder':_('زانیاری زیادە ٢')}),
            'info_3':forms.TextInput(attrs={'placeholder':_('زانیاری زیادە ٣')}),
            'qnt_in_box':forms.NumberInput(attrs={'placeholder':_('عەدەد لەناو کارتۆن')}),
            'kg_box':forms.NumberInput(attrs={'placeholder':_('کێشی کارتۆن')}),
            'kg_single':forms.NumberInput(attrs={'placeholder':_('کێشی دانە')}),

        }
    
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['part_group'].queryset = PartGroups.objects.all()
        # if 'category' in self.data:
        #     try:
        #         category_id = int(self.data.get('category'))
        #         self.fields['part_group'].queryset = PartGroups.objects.filter(category=category_id).all()
        #     except:
        #         pass
        
        # elif self.instance.pk:
        #     self.fields['part_group'].queryset = self.instance.category.part_group_set



