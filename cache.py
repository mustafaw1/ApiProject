import redis
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ApiProject.settings")
import django
django.setup()
from django.core.management import call_command
from faker import Faker
from django.core.serializers.json import DjangoJSONEncoder
fake = Faker()
from ApiApplication.models import Student
from ApiApplication.models import Person 
from django.http import JsonResponse

import json

from django.core import serializers

r = redis.Redis(host='localhost', port=6379)

person = serializers.serialize("json" , Person.objects.filter(id=1))
json_person = json.dumps(person)
person1 = str(Person.objects.get(id=1))
r.set(person1, json_person)
unpacked_person = json.loads(r.get(person1))
person = unpacked_person





print(person)

