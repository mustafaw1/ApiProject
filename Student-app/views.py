from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
from rest_framework.filters import SearchFilter
from django.core.cache import cache
import redis
import json


from datetime import timedelta

cache = redis.Redis(host="localhost", port=6379)


# Create your views here
# class from APIView


class PersonApiView(APIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        persons = Person.objects.all()
        return persons

    def get(self, request):
        id = request.query_params["id"]
        key = "person" + id
        if cache.get(key):
            person = cache.get(key)
            load_person = json.loads(person)
            return Response(load_person)
        else:
            person = Person.objects.get(id=id)
            serialized_person = PersonSerializer(person)
            json_person = json.dumps(serialized_person.data)
            cache.set(key, json_person, timedelta(seconds=5))
        return Response(serialized_person.data)

    def post(self, request):
        print("Request data is : ", request.data)
        serializer_obj = PersonSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            person = Person.objects.all().filter(id=request.data["id"]).values()
            return Response({"Message": "New Person Added!", "Person": person}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        id = request.query_params["id"]
        key = "perosn" + id
        person_object = Person.objects.get(id=id)
        serializer = PersonSerializer(person_object, data=request.data)             
        if serializer.is_valid():
            serializer.save()
            json_person = json.dumps(serializer.data)
            cache.set(key , json_person)
            return Response({"Message": "Full Person updated!"}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
               
    def patch(self, request):
        id = request.query_params["id"]
        key = "perosn" + id
        person_object = Person.objects.get(id=id)
        serializer = PersonSerializer(person_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            json_person = json.dumps(serializer.data)
            cache.set(key, json_person)
            return Response({"Message": "Partial Person updated!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# class for ModelView
class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    def get_queryset(self):
        student = Students.objects.all()
        return student


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    def get_queryset(self):
        course = Courses.objects.all()
        return course

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     print(params['pk'])
    #     params_list = params['pk'].split('-')
    #     students1= Student.objects.filter(first_name__iexact = params_list[0], last_name__iexact = params_list[1])
    #     serializer = StudentSerializer(students1 ,many = True)
    #     return Response(serializer.data)


def Health(request):
    if request.method == "GET":
        # data = {
        #     "Hello":status.HTTP_200_OK
        # }
        return HttpResponse("hello", status.HTTP_200_OK)
