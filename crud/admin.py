from django.contrib import admin

# Register your models here.
from crud.models import Lecturer, Course, Venue, InvigilatorTimetable

admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(Venue)
admin.site.register(InvigilatorTimetable)
