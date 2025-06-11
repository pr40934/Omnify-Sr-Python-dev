from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Event, Attendee

class EventAPITest(APITestCase):
    def setUp(self):
        self.event = Event.objects.create(
            name="Test Event",
            location="Test Location",
            start_time="2025-06-11T10:00:00Z",
            end_time="2025-06-11T12:00:00Z",
            max_capacity=2
        )

    def test_create_event(self):
        url = reverse('event-list-create')
        data = {
            "name": "New Event",
            "location": "Location X",
            "start_time": "2025-07-01T10:00:00Z",
            "end_time": "2025-07-01T12:00:00Z",
            "max_capacity": 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_attendee_success(self):
        url = reverse('event-register', args=[self.event.id])
        data = {"name": "John Doe", "email": "john@example.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_attendee_duplicate_email(self):
        url = reverse('event-register', args=[self.event.id])
        data = {"name": "John Doe", "email": "john@example.com"}
        self.client.post(url, data, format='json')  # first registration
        response = self.client.post(url, data, format='json')  # duplicate
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Already registered', response.data['error'])

    def test_register_attendee_event_full(self):
        url = reverse('event-register', args=[self.event.id])
        self.client.post(url, {"name": "A", "email": "a@example.com"}, format='json')
        self.client.post(url, {"name": "B", "email": "b@example.com"}, format='json')
        data = {"name": "C", "email": "c@example.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Event is full', response.data['error'])

    def test_get_attendees(self):
        url_register = reverse('event-register', args=[self.event.id])
        self.client.post(url_register, {"name": "John", "email": "john@example.com"}, format='json')
        url_attendees = reverse('attendee-list', args=[self.event.id])
        response = self.client.get(url_attendees)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
