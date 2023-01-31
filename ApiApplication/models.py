from django.db import models


from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    age = models.IntegerField(max_length=20)
    city = models.CharField(max_length=200)

    class Meta:
       indexes = [models.Index(fields=['name', 'age'])]

class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_duration = models.IntegerField(max_length=10)
    class_room = models.IntegerField(max_length=5)

    def __str__(self):
        return self.course_name


class Students(models.Model):
    profile_image = models.ImageField(upload_to='Images', default='None.jpg')
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=200)
    grade = models.CharField(max_length=100)
    courses = models.ManyToManyField(Courses, related_name='course')

    def __str__(self):
        return self.name

