import json
from UsersRestApi.models import User
from UsersRestApi.serializers import UserSerializer
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid()
        user_serializer.save()
  
        return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 

    elif request.method == 'GET':
        # attempt to get the user with given id from mongodb
        return HttpResponse(
            json.dumps({'request-type': request.method}), 
            content_type="application/json"
        )
    elif request.method == 'DELETE':
        # attempt to delete the user with given id from mongodb
        return HttpResponse(
            json.dumps({'request-type': request.method}),
            content_type="application/json"
        )
