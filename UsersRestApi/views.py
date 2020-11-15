from . import mongodb_interface as mongodb
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from rest_framework.parsers import JSONParser
from pymongo import MongoClient
import json


@csrf_exempt
def retrieve_user(request, id):
    id = request.GET.get('id')
    if request.method == 'GET':
        user = mongodb.retrieve(id)
        return HttpResponse(
            json.dumps(user),
            content_type="application/json"
        )
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_id = mongodb.update(id, request)
        return HttpResponse(
            json.dumps({'user-id': f"{user_id}"}),
            content_type="application/json"
        )
    elif request.method == 'DELETE':
        mongodb.delete(id)
        return HttpResponse(
            status=204,
            content_type="application/json"
        )


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_id = mongodb.insert(user_data)
        return HttpResponse(
            json.dumps({'user-id': f"{user_id}"}),
            content_type="application/json"
        )
