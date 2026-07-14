from django.urls import path
from .views import SchoolListCreateView, SchoolRetrieveUpdateView, SchoolNearbyListView,ClassRoomListCreateView

app_name = "api-v1"
urlpatterns = [
    path("schools/", SchoolListCreateView.as_view(), name= "school_list_create"),
    path("schools/<int:pk>", SchoolRetrieveUpdateView.as_view(), name= "school_retrieve_update"),
    path("schools/nearby/",SchoolNearbyListView.as_view() , name="school_nearby"),
    path("schools/new_class/", ClassRoomListCreateView.as_view(), name="new_class")
]