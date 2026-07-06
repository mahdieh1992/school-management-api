from django.db import models

# Create your models here.

class School(models.Model):
    """    school model stores information about schools
    """
    name = models.CharField(max_length= 150)
    latitude = models.DecimalField(max_digits= 9, decimal_places= 6, blank= True, null= True)
    longitude = models.DecimalField(max_digits= 9, decimal_places= 6, blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name