from .scheduler import run_jobs
from threading import Thread

def start_job_thread():
    job_thread = Thread(target=run_jobs)
    job_thread.daemon = True  
    job_thread.start()
