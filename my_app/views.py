from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from my_app.models import Student
from my_app.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status


class StudentListCreate(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Instance created successfully'
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                'message': 'Can not be created',
                'data': serializer.data
            }, status = status.HTTP_400_BAD_REQUEST)

class StudentDetailUpdateDelete(APIView):

    def get(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data) 

    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Instance updated successfully'
            }, status = status.HTTP_202_ACCEPTED)
        else:
            return Response({
                'message': 'Can not be updated. Please check your data.',
                'data': serializer.data
            }, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({
                'message': 'Instance deleted successfully'
            }, status = status.HTTP_202_ACCEPTED)

# Alternative Responses:
# return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------------------------------------------
# Yukarıdaki işlemleri tek class'da yazmaya çalışalım

# class StudentGPPD(APIView):

#     def get(self, request, pk=0):
#         if pk:
#         # Tek kayıt görüntüle:
#             student = get_object_or_404(Student, id=pk)
#             serializer = StudentSerializer(instance=student)
#             return Response(serializer.data)
#         else:
#         # Kayıtları listele:
#             students = Student.objects.all()
#             serializer = StudentSerializer(instance=students, many=True)
#             return Response(serializer.data)
    
#     # Yeni Kayıt (POST Method)
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # Tek kayıt güncelle:
#     def put(self, request, pk):
#         student = get_object_or_404(Student, id=pk)
#         serializer = StudentSerializer(instance=student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     # Tek kayıt sil:
#     def delete(self, request, pk):
#         student = get_object_or_404(Student, id=pk)
#         student.delete()
#         return Response({ "message": "Deleted" }, status=status.HTTP_204_NO_CONTENT)




# ----------------------------------------------------------------
# GenericAPIView
# https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview
# Mixins
# https://www.django-rest-framework.org/api-guide/generic-views/#mixins
# ListCreateAPIView
# RetrieveUpdateDestroyAPIView
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
# ----------------------------------------------------------------


from rest_framework.generics import GenericAPIView
from rest_framework import mixins
class StudentGenericListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Bu işlemler için bir yol daha var.

# ----------------------------------------------------------------
# ListCreateAPIView

# RetrieveUpdateDestroyAPIView

# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
# ----------------------------------------------------------------

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = "id" # Default: "pk" olarak ayarlı. Değiştirilebilir bu şekilde.



# ----------------------------------------------------------------
# ModelViewSet:

# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset

# ----------------------------------------------------------------
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

# Tüm İşlemleri yapar.....
class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    # özel veri istendiğinde, aşağıdaki decorator eklenebilir.
    # Mesela öğrenci sayısı
    @action(methods=["GET"], detail=False)
    def count(self, request):
        return Response({
            "count": Student.objects.count()
        })
