from django.urls import path
from .views import StudentListCreate, StudentDetailUpdateDelete

urlpatterns = [
    path("student_list_create/", StudentListCreate.as_view()), # 1
    path("student_detail_update_delete/<int:pk>", StudentDetailUpdateDelete.as_view()),
]

# 1 Bir URL çağırıldığında bir fonksiyon çalışır. Ancak bu bir fonk değil. Bir method. Class içindeki fonksiyonlar bir metottur.
