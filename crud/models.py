from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Lecturer(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=256)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    number_of_candidates = models.IntegerField(default=0)
    course_code = models.CharField(max_length=5)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class InvigilatorTimetable(models.Model):
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    examiner = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name='examiner')
    invigilator = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name='invigilator')

    def __str__(self):
        return self.course_code
