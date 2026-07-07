from django.db import models
from django.contrib.auth import get_user_model
from ..school.models import BaseModel

# Create your models here.
User = get_user_model()

class Message(BaseModel):
    """
        Stores messages sent between users.
    """
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete= models.CASCADE, related_name="messages")
    
    def __str__(self):
        return self.text
    

class MessageReceiver(models.Model):
    """
        Stores the read status of messages for each recipient.
    """
    message = models.ForeignKey(Message, on_delete= models.CASCADE, related_name="message_receivers")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_receivers")
    is_read = models.BooleanField(default=False)
    read_date = models.DateTimeField(blank= True, null= True)
    
    def __str__(self):
        return f"{self.user.email} - {self.message.text[:30]}"
    
    
    