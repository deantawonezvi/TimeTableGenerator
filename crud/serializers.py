from rest_framework import serializers

from crud.models import Lecturer, Course, Venue, InvigilatorTimetable


class LecturersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('id', 'name', 'surname', 'email')


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'number_of_candidates', 'lecturer_id', 'lecturer')


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ('name', 'capacity')


class InvigilatorTimetableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvigilatorTimetable
        fields = ('start_date', 'end_date', 'course_code', 'venue', 'examiner', 'invigilator')
