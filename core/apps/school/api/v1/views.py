from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from ...models import School, ClassRoom
from .serializers import SchoolSerializer, NearbySchoolSerializer, ClassSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from geopy.distance import geodesic
User = get_user_model()

class SchoolListCreateView(ListCreateAPIView):
    """
        List and create schools.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_permissions(self):
        """
             Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    
    
    
class SchoolRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update and Delete a school.
    """
    permission_classes = [IsAdminUser]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class SchoolNearbyListView(APIView):
    """
        List of nearby school for teacher and students
    """
    def get(self, request):
        nearby_school = []
        schools = School.objects.all()
        user = self.request.user
        user_geo = (user.profile.latitude, user.profile.longitude)
        for school in schools:
            school_geo = (school.latitude, school.longitude)
            nearby = {
                'name': school.name,
                'distance': geodesic(school_geo, user_geo).km 
             }
            nearby_school.append(nearby)
        serializer = NearbySchoolSerializer(nearby_school, many=True)
        return Response(serializer.data)
    
class ClassRoomListCreateView(ListCreateAPIView):
    """
        Provides APIs for listing classrooms and creating new classrooms.
        
        Only administrators can create and manage classrooms.
    """
    permission_classes = [IsAdminUser]
    queryset = ClassRoom.objects.all()
    serializer_class = ClassSerializer
    
    