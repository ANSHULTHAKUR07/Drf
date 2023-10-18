from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer
from.serializers import TagsSerializer
from.serializers import TaskSerializer
from.serializers import UserGetSerializer
from rest_framework import exceptions
from rest_framework import status
from rest_framework.response import Response
from.models import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import logout
from rest_framework import generics
from.permissions import UserPermission
# Create your views here.

class UserAPIView(APIView):
    # authentication_classes = [BasicAuthentication]
    serializer_class = [UserCreateSerializer, UserGetSerializer]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        print(request.user)
        user = User.objects.all()
        if not user:
            raise exceptions.JsonResponse(detail={"user":"user doesn't exist"}, code=status.HTTP_204_NO_CONTENT)
        serializer = UserGetSerializer(user,many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = UserCreateSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            user = User.objects.create(username=data["username"], password=request_data["password"])
            user.set_password(request_data["password"])
            user.save()
            return Response(serializer.data)
        

class CheckAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print("check url in Checkapivuew class ")


class TagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('pk')
        tags = Tags.objects.filter(id=id).first()
        if not tags:
            raise exceptions.JsonResponse(detail={"tags":"tags doesn't exist"}, code=status.HTTP_204_NO_CONTENT)
        
        serializer = TagsSerializer(tags)
        return  Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        valid_data = TagsSerializer(data=data)
        if valid_data.is_valid(raise_exception=True):
            valid_data.save()
            return Response(valid_data.data)
        

class TaskAPIView(APIView):

    def get(self, request, *args, **kwargs):
        id = request.GET.get('pk')
        task_data = Task.objects.filter(id=id).first()

        if not task_data:
            raise exceptions.JsonResponse(detail={"task":"task doesn't exist"}, code=status.HTTP_204_NO_CONTENT)
        
        serializer = TaskSerializer(task_data)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        valid_data = TaskSerializer(data=data)
        if valid_data.is_valid(raise_exception=True):
            valid_data.save()
            return Response(valid_data.data)
        

# class LoginAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         request_data = request.data
#         print(request_data["username"], request_data["password"])
#         serializer = UserLoginSerializer(data=request_data)

#         if serializer.is_valid(raise_exception=True):
#             data = serializer.validated_data()
#             user = User.objects.get(username=data["username"], password=["password"])
#             if not user:
#                 raise exceptions.JsonResponse(detail={"user":"user doesn't exist"}, code=status.HTTP_204_NO_CONTENT)
            
#             return Response(user.data)
        

class LogoutAPIView(APIView):
    def get(self, request, *args, **kwars):
        logout(request)

        return Response({"detail":"logout successfully"})
    
class checkAPIView(generics.ListCreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [UserPermission]
    queryset = User.objects.all()
    fields = "__all__"
        

class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class RetrieveDleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserCreateSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()


class RetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserCreateSerializer
    lookup_field = "pk"
    queryset = User.objects.all()


class RetriveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = UserCreateSerializer
    lookup_field = "pk"
    queryset = User.objects.all()

from rest_framework import viewsets,mixins
from rest_framework.decorators import action


class TaskGenericViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @action(method='GET',detail=False)
    def get_filtered_tasks(self, request, *args, **kwargs):
        tasks = super().get_queryset()
        data =tasks.filter(id=request.GET.get('pk')).first()
        print(data.__dict__, "task data")
        serializer = TaskSerializer(data)
        return Response(serializer.data)


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = UserCreateSerializer
    
    
    



    

    
