def schedule_jobs():
    num_jobs = int(input("Enter the number of jobs: "))
    jobs = {}
    for i in range(num_jobs):
        job_name = input(f"Enter name of job {i+1}: ")
        job_duration = int(input(f"Enter duration of job {i+1} (in minutes): "))
        jobs[job_name] = job_duration
        
    sorted_jobs = dict(sorted(jobs.items(), key=lambda x: x[1]))
    
    print("\nScheduled Jobs:")
    for job, duration in sorted_jobs.items(): 
        print(f"{job}: (duration) minutes")

#Call the function to schedule jobs

schedule_jobs()