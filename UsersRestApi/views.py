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
def retrieve_user(request, id):
    id = request.GET.get('id')
    if request.method == 'GET':
        user = retrieve(id)
        return HttpResponse(
            json.dumps(user),
            content_type="application/json"
        )
    elif request.method == 'DELETE':
        # attempt to delete the user with given id from mongodb
        return HttpResponse(
            json.dumps({'request-type': request.method}),
            content_type="application/json"
        )


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_id = insert(user_data)
        return HttpResponse(
            json.dumps({'user-id': f"{user_id}"}),
            content_type="application/json"
        )


def create_mongo_connection():
    return MongoClient('mongodb://localhost:27017')


def get_users_table(client):
    db = client['users_db']
    return db.users


def insert(user):
    client = create_mongo_connection()
    users_table = get_users_table(client)
    return users_table.insert_one(user).inserted_id


def retrieve(id):
    client = create_mongo_connection()
    users_table = get_users_table(client)
    user = users_table.find_one({'id': id})
    user['_id'] = str(user.get('_id'))
    return user

def delete(id):
    client = create_mongo_connection()
    users_table = get_users_table(client)
    user = users_table.delete_one({'id': id})
    user['_id'] = str(user.get('_id'))
    return user