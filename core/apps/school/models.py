from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class BaseModel(models.Model):
    """
         Abstract base model containing common timestamp fields.
    """
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    class Meta:
        abstract = True
    

class School(BaseModel):
    """    school model stores information about schools
    """
    name = models.CharField(max_length= 150)
    latitude = models.DecimalField(max_digits= 9, decimal_places= 6, blank= True, null= True)
    longitude = models.DecimalField(max_digits= 9, decimal_places= 6, blank= True, null= True)
   
    def __str__(self):
        return self.name
    
class Lesson(BaseModel):
    """
        Lesson model stores information about lessons.
    """
    title = models.CharField(max_length= 150)
    code = models.CharField(max_length= 100, unique= True)
    
    def __str__(self):
        return self.title
    
class ClassRoom(BaseModel):
    """
        ClassRoom model stores information about each class 
    """
    name = models.CharField(max_length= 150)
    lesson = models.ForeignKey(Lesson, on_delete= models.CASCADE, related_name="classes")
    teacher = models.ForeignKey(User, on_delete= models.CASCADE, related_name="teacher_classes")
    student = models.ManyToManyField(User, related_name="student_classes")
    school = models.ForeignKey(School, on_delete= models.CASCADE, related_name= "classes")
    
    def __str__(self):
        return self.name
    
    