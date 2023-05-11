from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# def home(request):
#     return HttpResponse('Welcome to Home Page')

"""
*******@api_view()***********
Decorator that converts a function-based view into an APIView subclass.
Takes a list of allowed methods for the view as an argument.
"""
@api_view()
def home(request):
    return Response(
        {
            'message': 'Welcome to App Home Page'
        }
    )

def project_home(request):
    return HttpResponse('Welcome to Project Home Page')