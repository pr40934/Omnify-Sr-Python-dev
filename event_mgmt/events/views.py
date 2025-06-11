from rest_framework import generics, status
from rest_framework.response import Response
from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer

# GET And POST
class EventListCreateView(generics.ListCreateAPIView): # Auto save's in the model
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# POST
class RegisterAttendeeView(generics.CreateAPIView):
    serializer_class = AttendeeSerializer

    def create(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=404)

        if event.attendees.count() >= event.max_capacity:
            return Response({'error': 'Event is full'}, status=400)

        # Email validation.
        if Attendee.objects.filter(event=event, email=request.data.get('email')).exists():
            return Response({'error': 'Already registered with this email'}, status=400)

        attendee = Attendee(event=event, name=request.data.get('name'), email=request.data.get('email'))
        attendee.save()
        return Response(AttendeeSerializer(attendee).data, status=201)

# GET
class AttendeeListView(generics.ListAPIView):
    serializer_class = AttendeeSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Attendee.objects.filter(event__id=event_id)
