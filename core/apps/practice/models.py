from django.db import models
from django.contrib.auth import get_user_model
from ..school.models import ClassRoom, BaseModel

User = get_user_model()
# Create your models here.

class Practice(BaseModel):
    """
        Stores assignments created for a classroom.
    """
    title = models.CharField(max_length= 150)
    body = models.TextField(blank= True, null= True)
    deadline = models.DateTimeField()
    attachment = models.FileField(upload_to="documents/", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="practices")
    class_room = models.ForeignKey(ClassRoom, on_delete= models.CASCADE, related_name="practices")
    
    def __str__(self):
        return self.title
    
    
class PracticeAnswer(BaseModel):
    """
         Stores students' answers submitted for assignments.
    """
    practice = models.ForeignKey(Practice, on_delete= models.CASCADE, related_name="practice_answers")
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="practice_answers")
    answer = models.TextField(blank= True, null= True)
    attachment = models.FileField(upload_to="documents/", blank=True, null=True)
    
    def __str__(self):
        return self.practice.title
    
    