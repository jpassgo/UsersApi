import json
from .models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        # create new user and add to mongodb
        name = body['name']
        email = body['email']
        age = body['age']

        User(name, email, age)
        return HttpResponse(
            json.dumps({'request-type': request.method}),
            content_type="application/json")
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
