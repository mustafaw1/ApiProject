import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ApiProject.settings")

import django

django.setup()
from django.core.management import call_command
from faker import Faker

fake = Faker()
from ApiApplication.models import Student
from ApiApplication.models import Person
import random
from faker.providers import BaseProvider



def populate_person(value):
    bulk_list = list()
    for i in range(value):
        id = i
        name = fake.name()
        age = random.randint(0, 100)
        city = fake.city()
        bulk_list.append(Person(id = id, name = name, age = age, city = city))
    obj = Person.objects.bulk_create(bulk_list)


def populate_student(value):
    for i in range(value):
        id = i
        first_name = fake.name()
        last_name = fake.name()
        dob = fake.date()
        obj = Student.objects.get_or_create(
            id=id, first_name=first_name, last_name=last_name, dob=dob
        )


def main():
    no = int(input("how many records you want to send: "))
    populate_person(no)
    # populate_student(no)


if __name__ == "__main__":
    main()
