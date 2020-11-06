from UsersRestApi.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from UsersRestApi.models import User
from django.shortcuts import render
from pymongo import MongoClient
import json


@csrf_exempt
def user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        print(user_data)

        client = MongoClient('mongodb://localhost:27107')
        db = client['users_db']
        users_table = db.users
        users_table.insert_one(post_data)
  
        return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 

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



def create_mongo_connection():
    client = MongoClient('mongodb://localhost:27107')
    db = client['users_db']
    return db.users