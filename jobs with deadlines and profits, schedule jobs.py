import heapq

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

    def _lt_(self, other):      ## method is used to compare jobs based on their profit. This method is useful when sorting jobs by their profit, so jobs with higher profits are given priority.
        return self.profit > other.profit  

def job_scheduling(jobs):
    
    # jobs.sort(key=lambda job: job.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)  
    result = [-1] * (max_deadline + 1)  
    print('result',result)

    max_profit = 0
    job_count = 0
    for job in jobs:
        for slot in range(min(max_deadline, job.deadline), 0, -1):
            if result[slot] == -1:  
                result[slot] = job.job_id
                max_profit += job.profit
                job_count += 1
                break

    scheduled_jobs = [job_id for job_id in result if job_id != -1]
    return job_count, max_profit, scheduled_jobs


jobs = [
    ##  id   dline  profit
    Job("A",   2,   100),
    Job("B",   1,   50),
    Job("C",   2,   20),
    Job("D",   1,   40),
    Job("E",   3,   30)
]
 
count, profit, scheduled_jobs = job_scheduling(jobs)
print(f"Total Jobs Scheduled: {count}")
print(f"Total Profit: {profit}")
print(f"Scheduled Jobs Order: {scheduled_jobs}")














import heapq

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit
    
    # For max heap, we reverse the comparison to prioritize high profit jobs
    def __lt__(self, other):
        return self.profit > other.profit

def job_scheduling(jobs):
    # Step 1: Sort the jobs by profit (using a heap)
    #jobs.sort(key=lambda job: job.profit, reverse=True)
    heapq.heapify(jobs)  ##sort by profit in descending order
    
    # Step 2: maximum num of deadlines
    max_deadline = max(job.deadline for job in jobs)
    
    # Step 3: Create an array to track which slots are filled
    slots = [-1] * (max_deadline + 1)  # Using -1 to indicate unfilled slots
    total_profit = 0
    job_count = 0
    
    # Step 4: Try to schedule each job
    while jobs:
        job = heapq.heappop(jobs)  # Get the job with the highest profit
        # Try to place the job in the latest available slot before its deadline
        for slot in range(job.deadline, 0, -1):
            if slots[slot] == -1:  # If the slot is free
                slots[slot] = job.job_id  # schedule job in the slot
                total_profit += job.profit  # Add the profit
                job_count += 1  # Increase the job count
                break

    # Collect the scheduled job ids
    scheduled_jobs = [job_id for job_id in slots if job_id != -1]
    
    return job_count, total_profit, scheduled_jobs

# List of jobs (job_id, deadline, profit)
jobs = [
    Job("A", 2, 100),
    Job("B", 1, 50),
    Job("C", 2, 20),
    Job("D", 1, 40),
    Job("E", 3, 30)
]

# Call the job scheduling function
count, profit, scheduled_jobs = job_scheduling(jobs)

# Output the results
print(f"Total Jobs Scheduled: {count}")
print(f"Total Profit: {profit}")
print(f"Scheduled Jobs Order: {scheduled_jobs}")
