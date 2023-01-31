from django.contrib import admin
from .models import Students
from .models import Person
from .models import Courses

admin.site.register(Person)
admin.site.register(Students)
admin.site.register(Courses)

# Register your models here.
