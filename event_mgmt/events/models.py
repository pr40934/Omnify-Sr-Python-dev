from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField()

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        unique_together = ('event', 'email')  # prevent duplicate
