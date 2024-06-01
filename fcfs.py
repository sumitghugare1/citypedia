def fcfs_scheduling(burst_times):
    n = len(burst_times)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_times[i - 1]
    
    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_times[i]
    
    # Print process information
    print("Processes    Burst Time    Waiting Time    Turnaround Time")
    for i in range(n):
        print(f"P{i+1}           {burst_times[i]}              {waiting_time[i]}              {turnaround_time[i]}")
    
    # Calculate average waiting time and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Example burst times
burst_times = [4, 3, 1, 2, 5]

fcfs_scheduling(burst_times)
