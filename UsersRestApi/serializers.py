from rest_framework import serializers
from UsersRestApi.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'age')