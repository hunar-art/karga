from django.contrib.auth.models import User
from django.db import models
from django.db.models import constraints
from django.db.models.base import Model
from users.models import UserAccount

class MainGroup(models.Model):
    admin = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    main_type = models.CharField(max_length=40,unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_type

    class Meta:
        db_table = 'maingroup'

class PartGroups(models.Model):
    admin = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    main_type = models.ForeignKey(MainGroup,on_delete=models.PROTECT,related_name='maintypes')
    part_group = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.part_group

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['main_type','part_group'],name='unique_fields')
        ]
        db_table = 'partgroups'


class ProductGroup(models.Model):
    admin = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    product_group = models.CharField(max_length=50,unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_group

    class Meta:
        db_table = 'productgroup'

class Products(models.Model):
    admin = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    category = models.ForeignKey(MainGroup,on_delete=models.PROTECT,related_name='category')
    part_group = models.ForeignKey(PartGroups,on_delete=models.PROTECT,related_name='partgroup')
    product_group = models.ForeignKey(ProductGroup,on_delete=models.PROTECT,related_name='productgroup')
    product_name = models.CharField(max_length=40,unique=True)
    qnt_in_box = models.IntegerField()
    kg_single = models.DecimalField(max_digits=20,decimal_places=2)
    kg_box = models.DecimalField(max_digits=20,decimal_places=2)
    info_1 = models.CharField(max_length=100,blank=True,null=True)
    info_2 = models.CharField(max_length=100,blank=True,null=True)
    info_3 = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category','part_group','product_group'],name='unique_info')
        ]
        db_table = 'products'



