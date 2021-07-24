from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

class AccountManager(BaseUserManager):
    def create_user(self,username,password=None,is_active=True,is_staff=True,is_superuser=False):
        if not username:
            raise ValueError(_('تکایە ناوی کارمەند بنوسە!'))
        if not password:
            raise ValueError(_('تکایە وشەی نهێنی بنوسە!'))
        
        user_obj = self.model(
            username=username,
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self,username,password=None):
        user = self.create_user(
            username = username,
            password = password,
            is_staff=True
        )
        return user
    
    def create_superuser(self,username,password=None):
        user = self.create_user(
            username=username,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        return user

class UserPermission(models.Model):
    type_of_permission = models.CharField(max_length=30,unique=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.type_of_permission
    
    class Meta:
        db_table = 'user_permission'

def image_profile(instance,filename):
    username = instance.username
    slug = slugify(username)
    return f'admins/{slug}'


class UserAccount(AbstractBaseUser):
    username = models.CharField(max_length=80,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    permis = models.ManyToManyField(UserPermission,blank=True)
    image = models.ImageField(upload_to=image_profile,blank=True,null=True)
    objects = AccountManager()

    USERNAME_FIELD = 'username'

    def get_short_name(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.superuser
