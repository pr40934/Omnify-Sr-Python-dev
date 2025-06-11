from django.urls import path
from .views import EventListCreateView, RegisterAttendeeView, AttendeeListView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:event_id>/register/', RegisterAttendeeView.as_view(), name='event-register'),
    path('events/<int:event_id>/attendees/', AttendeeListView.as_view(), name='attendee-list'),
]
