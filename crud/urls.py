from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'lecturers', views.LecturerViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'venues', views.VenueViewSet)
router.register(r'timetable', views.InvigilatorTimetableViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]