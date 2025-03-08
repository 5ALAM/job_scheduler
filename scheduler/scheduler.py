import heapq
from datetime import timedelta
from django.utils import timezone
from .models import Job
import time

MAX_RUNNING_JOBS = 4


PRIORITY_LEVELS = {
    'High': 1,
    'Medium': 2,
    'Low': 3
}

def run_jobs():
    while True:
        pending_jobs = Job.objects.filter(status='Pending')

        job_queue = []

        for job in pending_jobs:
            job_priority = PRIORITY_LEVELS.get(job.priority, 3)  
            job_deadline = job.deadline 

   
            heapq.heappush(job_queue, (job_priority, job_deadline, job.id))

        running_jobs = Job.objects.filter(status='Running')
        running_jobs_count = running_jobs.count()

        if running_jobs_count < MAX_RUNNING_JOBS and job_queue:
            _, _, job_id = heapq.heappop(job_queue)
            job_to_run = Job.objects.get(id=job_id)

            job_to_run.status = 'Running'
            job_to_run.start_time = timezone.now()
            job_to_run.save()

            simulate_job_work(job_to_run)

            job_to_run.status = 'Completed'
            job_to_run.end_time = timezone.now()
            job_to_run.save()

        time.sleep(5)

def simulate_job_work(job):
    time.sleep(job.estimated_duration)
