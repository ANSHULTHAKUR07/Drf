from rest_framework import serializers
from django.contrib.auth.models import User
from.models import *
import re


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ("tag_name",)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    # def create(self, validated_data): 
    #     task_data = Task.objects.all()
class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_active','is_staff')
        

class UserCreateSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_active','is_staff','task')

    def to_representation(self, instance):
        print(instance, "user instance")
        instance_dict = UserGetSerializer(instance)
        task_queryset = Task.objects.filter(user=instance.id)
        serializer = TaskSerializer(task_queryset,many=True)
        print(serializer.data, "serializer data")
        

        # extract data from serilizer
        task_data = serializer.data  
        # convert serilizer data into dictionary
        instance_data = instance_dict.data
        # add task_data into USer instance 
        instance_data['task'] = task_data
        print(instance_data, "instance dict data in to representive method !!!!")
        return instance_data

    def create(self, validated_data): 
        task = validated_data.pop('task')
        tag=task[0].pop('tag')
        user_save = User.objects.create(username=validated_data.get("username"), password=validated_data.get("password"))
        user_save.set_password(validated_data.get("password"))
        user_save.save()
        for task_data in task:
            print(task_data, "user data in for lop")
            # tags_id = task.data.pop('tags_id', [])
            task_obj = Task.objects.create(user= user_save, **task_data)
            task_obj.tag.set(tag)
        return user_save
    
    def update(self, instance,validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        validated_data['password']=instance.password
        data = super().update(instance,validated_data)
        return data
    
    # def validate(self, data):
    #     """ object level validation """
    #     password = data['password']
    #     username = data['username']
    #     email = data['email']
    #     if not username.isalpha():
    #         raise serializers.ValidationError("usrname only containe alphabate")
    #     email_rexpression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    #     if (re.fullmatch(email_rexpression, email)):
    #         pass
    #     else:
    #         raise serializers.ValidationError("Invalid email")
    #     if len(password)<5 or len(password)>15:
    #         raise serializers.ValidationError("password must be between 5 and 15 character !!!")
    #     elif re.search('[0-9]',password) is None:
    #         raise serializers.ValidationError("Password denied: must contain a number between 0 and 9")
    #     elif re.search('[A-Z]',password) is None:
    #         raise serializers.ValidationError("Password denied: must contain a capital letter.")
    #     elif re.search('[a-z]',password) is None:
    #         raise serializers.ValidationError("Password denied: must contain a lowercase letter.")
    #     return data
    
    def validate_username(self, value):
        """field level validations """
        if not value.isalpha():
            raise serializers.ValidationError("usrname only contain aplhabets !!!! ")
        return value
        

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','is_active')

    





    

    






