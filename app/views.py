# Create your views here.
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.request import Request


@api_view(['GET'])
def hello_world(request: Request):
    return JsonResponse({'message': 'Hello, World!'})
