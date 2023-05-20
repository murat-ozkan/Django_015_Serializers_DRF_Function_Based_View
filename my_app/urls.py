from django.urls import path
# from .views import home
from .views import (
    home,
    student_list,
    student_create,
    student_detail,
)

urlpatterns = [
    path('', home),
    path('student_list/', student_list), # listing
    path('student_create/', student_create), # new
    path('student_detail/<int:pk>', student_detail), # detailed info of a student. 
]

# küçük büyük işareti içerisinde, Veri göndermek istediğimizde, veri tipi ve ismi.