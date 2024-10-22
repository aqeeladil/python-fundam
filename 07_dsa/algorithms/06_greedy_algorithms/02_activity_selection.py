

# Activity Selection Problem

# Problem Statement: Given a set of activities with their start and end times, select the 
# maximum number of activities that don’t overlap.

def activity_selection(start_times, end_times):
    n = len(start_times)
    activities = list(zip(start_times, end_times))
    activities.sort(key=lambda x: x[1])  # Sort by end time
    
    selected_activities = []
    last_end_time = -1
    
    for activity in activities:
        if activity[0] >= last_end_time:
            selected_activities.append(activity)
            last_end_time = activity[1]
    
    return selected_activities

# Example usage:
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
print(activity_selection(start_times, end_times))  # Output: [(1, 2), (3, 4), (5, 7), (8, 9)]
