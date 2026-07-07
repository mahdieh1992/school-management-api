from django.db import models
from ..school.models import BaseModel, ClassRoom
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class News(BaseModel):
    """
        Stores news published for a classroom.
    """
    title = models.CharField(max_length= 150)
    body = models.TextField(blank= True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")
    class_room = models.ForeignKey(ClassRoom ,on_delete= models.CASCADE, related_name= "news")
    
    def __str__(self):
        return self.title
    

class NewsReceiver(models.Model):
    """
         Stores the read status of news for each student.
    """
    news = models.ForeignKey(News, on_delete= models.CASCADE, related_name="news_receivers")
    student = models.ForeignKey(User, on_delete= models.CASCADE, related_name="news_receivers")
    is_read = models.BooleanField(default= False)
    read_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.news.title
    
    
    