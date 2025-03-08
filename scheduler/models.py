from django.db import models
from django.contrib.auth.models import User 

class Job(models.Model):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    job_name = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=10, default='Pending')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    estimated_duration = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Job {self.id} - {self.job_name} - {self.priority}"
