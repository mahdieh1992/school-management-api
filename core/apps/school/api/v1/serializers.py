from rest_framework import serializers
from ...models import School
from ...models import ClassRoom

class SchoolSerializer(serializers.ModelSerializer):
    """
        Serializer for the School model.
    """
    class Meta:
        model = School
        fields = "__all__"
        
class NearbySchoolSerializer(serializers.Serializer):
    """
        Serializer for nearby schools with calculated distance.
    """
    name = serializers.CharField(max_length = 100)
    distance = serializers.FloatField()
    
    
class ClassSerializer(serializers.ModelSerializer):
    """
        Serializer for new class and assign teacher 
    """
    class Meta:
        model = ClassRoom
        fields = '__all__'