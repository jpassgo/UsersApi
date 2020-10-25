import json
from .models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from serializers import UserSerializer


@csrf_exempt
def user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        user_serializer.save()
        body = json.loads(request.body)
        # create new user and add to mongodb
        name = body['name']
        email = body['email']
        age = body['age']

        user = User(name, email, age)
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
