from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

@api_view()
def home(request):
    return Response(
        {
            'message': 'Hello World'
        }
    )

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(instance=students, many=True)
    # print(serializer)
    # print(dir(serializer))
    # print(serializer.data)
    print(students)
    return Response(serializer.data)


@api_view(['POST'])
def student_create(request):
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

