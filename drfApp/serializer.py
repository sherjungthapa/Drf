from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()
    message=serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def validate_age(self, age):
        if age>100 or age<0:
            raise serializers.ValidationError("age must be between ) to 100")
        return age
    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.age=validated_data.get("age",instance.age)
        instance.email=validated_data.get("email",instance.email)
        instance.message=validated_data.get("message",instance.message)
        instance.save()
        return instance