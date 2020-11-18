from rest_framework.parsers import JSONParser
from pymongo import MongoClient


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


def update(id, updated_user_attributes):
    client = create_mongo_connection()
    users_table = get_users_table(client)

    query = {"id": id}
    new_values = {"$set": updated_user_attributes}

    users_table.update_one(query, new_values)


def delete(id):
    client = create_mongo_connection()
    users_table = get_users_table(client)
    users_table.delete_one({'id': id})
