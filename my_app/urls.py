from django.urls import path
# from .views import home
from .views import (
    home,
    student_list,
    student_create,
    student_detail,
    student_update,
    student_delete,
    student_list_create,
    student_detail_update_delete,
)

urlpatterns = [
    path('', home),
    path('student_list/', student_list), # listing
    path('student_create/', student_create), # new
    path('student_detail/<int:pk>', student_detail), # detailed info of a student. 
    path('student_update/<int:pk>', student_update), # update
    path('student_delete/<int:pk>', student_delete), # delete
    # combine links
    path('student_list_create/', student_list_create),    
    path('student_detail_update_delete/<int:pk>', student_detail_update_delete),    
]

# küçük büyük <...> işareti içerisinde, Veri göndermek istediğimizde, veri tipi ve ismi.