from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


@api_view()
def home(request):
    return Response(
        {
            'message': 'Hello World'
        }
    )

@api_view(['GET'])
def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(instance=student, many=True)
    # print(serializer)
    # print(dir(serializer))
    # print(serializer.data)
    print(student)
    return Response(serializer.data)


@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    # print(Response.status_code)
    # print(status)
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

@api_view(["GET"])
def student_detail(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, id=pk) # hata dönmüyor, 404, "detail": "not found" dönüyor
    # serializer = StudentSerializer(instance=student)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(["PUT"])
def student_update(request, pk):
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

@api_view(["DELETE"])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return Response({
            'message': 'Instance deleted successfully'
        }, status = status.HTTP_202_ACCEPTED)


# Benzer fonsksiyonları birleştirelim
# id gerektirenleri bir yere toplayalım

@api_view(["GET", "POST"])
def student_list_create(request):
    if request.method == "GET": # listing
        student = Student.objects.all()
        serializer = StudentSerializer(instance=student, many=True)
        return Response(serializer.data)
    else:
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

@api_view(["GET", "PUT", "DELETE"])
def student_detail_update_delete(request, pk):
    student = get_object_or_404(Student, id=pk)

    match request.method:
        case "GET":
            serializer = StudentSerializer(student)
            return Response(serializer.data)            
        case "PUT":
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
        case "DELETE":
            student.delete()
            return Response({
                    'message': 'Instance deleted successfully'
                }, status = status.HTTP_202_ACCEPTED)
        case _:
            print("please be carefull :)")



# *********************************************************************
# from django.http import HttpResponse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# # def home(request):
# #     return HttpResponse('Welcome to Home Page')

# """
# *******@api_view()***********
# Decorator that converts a function-based view into an APIView subclass.
# Takes a list of allowed methods for the view as an argument.
# """
# @api_view()
# def home(request):
#     return Response(
#         {
#             'message': 'Welcome to App Home Page'
#         }
#     )

