from rest_framework import serializers

from rest_framework import serializers

from .models import *

# ApiView serializers
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'city']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'course_name', 'course_duration', 'class_room']


class StudentsSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True,
    queryset = Courses.objects.all()
    )
    class Meta:
        model = Students
        fields = ['id', 'profile_image', 'name', 'age', 'grade', 'courses']
        depth = 1