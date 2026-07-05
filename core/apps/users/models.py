from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
        Custom user model based on AbstractBaseUser
    """
    email = models.EmailField(_("email address"), unique= True)
    national_code = models.CharField(max_length= 10, blank= True, null= True, unique= True)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    is_deleted = models.BooleanField(default= False)
    is_registered = models.BooleanField(default= False)    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    

class Profile(models.Model):
    """
         Profile model stores additional user information beyond the default CustomUser model.
    """ 
    class Gender(models.TextChoices):
        FEMALE = "F", "Female"
        MALE = "M", "Male"
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE, related_name="profile")
    mobile_number = models.CharField(max_length= 11, blank= True, null= True)
    gender = models.CharField(max_length=1 , choices=Gender.choices, blank= True, null= True)
    image = models.ImageField(upload_to= 'users', blank= True, null= True)
    bio = models.TextField(blank= True, null= True)
    latitude = models.DecimalField(max_digits= 9, decimal_places= 6, blank= True, null= True)
    longitude = models.DecimalField(max_digits= 9, decimal_places= 6, blank= True, null= True)
    
    def __str__(self):
        return self.user.email
    
@receiver(post_save, sender=CustomUser)    
def save_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    