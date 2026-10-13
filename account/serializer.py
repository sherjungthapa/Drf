from rest_framework import serializers
from django.contrib.auth.models import User

class ResgisterSerialer(serializers.ModelSerializer):
    conform_password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password','conform_password']

    def validate(self, data):
        if data['password']!=data['conform_password']:
            raise serializers.ValidationError('password and conform_password dosenot matched')
        return data

    def create(self, validated_data):
        validated_data.pop('conform_password')
        return User.objects.create_user(**validated_data)