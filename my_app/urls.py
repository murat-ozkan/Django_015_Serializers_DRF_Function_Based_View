from django.urls import path
from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
    # StudentGPPD,
    StudentGenericListCreate,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('student_list_create/', StudentListCreate.as_view()),
    path('student_detail_update_delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
    # path('student_gppd/', StudentGPPD.as_view()),
    # path('student_gppd/<int:pk>', StudentGPPD.as_view()),
    path('student_generic_list_create/', StudentGenericListCreate.as_view()),
    path('student_list_create_api/', StudentListCreateAPIView.as_view()),
    path('student_get_put_delete_api/<int:pk>', StudentRetrieveUpdateDestroyAPIView.as_view()),
]

# 1 Bir URL çağırıldığında bir fonksiyon çalışır. Ancak bu bir fonk değil. Bir method. Class içindeki fonksiyonlar bir metottur.



# ----------------------------------------------------------------
# Router for ModelViewSet

from .views import StudentMVS
from rest_framework import routers

router = routers.DefaultRouter()

# Register the path
router.register('students', StudentMVS) # URL sonunda / yok. # router.register('another', AnotherMVS)

# Add to paths:
urlpatterns += router.urls

