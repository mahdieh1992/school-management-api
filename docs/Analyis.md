actor: admin                                     
action: create school
model: school
input: name, latitude, longitude
output: show info new school
serializer:
    field_name = ('name', 'latitude', 'longitude')
apiview:
    genericView
permission:
    admin only

--------------------------
actor: teacher
action: list school
model: school
input: ----
output: List of schools
serializer:
    field_name = ('name', 'latitude', 'longitude')
apiview:
    genericView

--------------------
actor: students
action: list school
model: school
input: -
output: List of schools
serializer:
    field_name = ('name', 'latitude', 'longitude')
apiview:
    genericView


--------------------------
Use Case:
List Schools
actor:
    Admin 
    Teachers
    Students
permissions:
    Authenticated
Output:
List of schools