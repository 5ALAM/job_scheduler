from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Job
from .forms import JobForm
from rest_framework import viewsets, permissions
from .serializers import JobSerializer
from .scheduler import run_jobs  # Import the run_jobs function directly
  # Importing the scheduler instance and run_jobs function


@login_required
def submit_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user  # Ensure the user is assigned
            if not job.status:  # Set the default status if not provided
                job.status = 'Pending'
            job.save()
            # return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'scheduler/job_form.html', {'form': form})


@login_required
def dashboard(request):
    jobs = Job.objects.filter(user=request.user)
    pending_jobs = jobs.filter(status='Pending')
    running_jobs = jobs.filter(status='Running')[:3]  
    completed_jobs = jobs.filter(status='Completed')
    
    from django.db.models import Avg, F, ExpressionWrapper, DurationField
    analytics = jobs.filter(status='Completed').aggregate(
        avg_wait_time=Avg(ExpressionWrapper(F('start_time') - F('created_at'), output_field=DurationField()))
    )
    
    context = {
        'pending_jobs': pending_jobs,
        'running_jobs': running_jobs,
        'completed_jobs': completed_jobs,
        'analytics': analytics,
    }
    return render(request, 'scheduler/dashboard.html', context)


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)
