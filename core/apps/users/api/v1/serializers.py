from rest_framework import serializers
from ...models import CustomUser

class UserSerializers(serializers.ModelSerializer):
    """
        Serializer for the User model.
    """
    model = CustomUser
    fields = '__all__'
    