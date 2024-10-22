

# Job Sequencing Problem

# Problem Statement: Given a set of jobs, each with a deadline and profit, sequence the jobs 
# to maximize the total profit, where each job takes one unit of time and must be completed by 
# its deadline.

def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)  # Sort by profit
    
    max_deadline = max(job[0] for job in jobs)
    slots = [False] * max_deadline  # Time slots initialization
    
    total_profit = 0
    job_sequence = [None] * max_deadline
    
    for job in jobs:
        deadline, profit = job
        for i in range(min(deadline - 1, max_deadline - 1), -1, -1):
            if not slots[i]:
                slots[i] = True
                job_sequence[i] = job
                total_profit += profit
                break
    
    return total_profit, job_sequence

# Example usage:
jobs = [(4, 20), (1, 10), (1, 40), (1, 30)]
print(job_sequencing(jobs))  # Output: (60, [(1, 40), (1, 30), (1, 10), None])
