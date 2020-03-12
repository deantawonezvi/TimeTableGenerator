from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import LecturersSerializer, CoursesSerializer, VenueSerializer, InvigilatorTimetableSerializer
from .models import Lecturer, Course, Venue, InvigilatorTimetable


class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all().order_by('name')
    serializer_class = LecturersSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CoursesSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all().order_by('name')
    serializer_class = VenueSerializer


class InvigilatorTimetableViewSet(viewsets.ModelViewSet):
    queryset = InvigilatorTimetable.objects.all().order_by('start_date')
    serializer_class = InvigilatorTimetableSerializer
