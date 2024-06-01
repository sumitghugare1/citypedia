def is_safe_state(available, allocation, max_need):
    num_processes = len(allocation)
    num_resources = len(available)

    # Calculate the need matrix
    need = [[max_need[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]
    
    # Initialize work and finish arrays
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                safe_sequence.append(i)
                finish[i] = True
                break
        else:
            return False, []

    return True, safe_sequence

# Example data
available = [3, 3, 2]
max_need = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Check if the system is in a safe state
is_safe, safe_sequence = is_safe_state(available, allocation, max_need)

if is_safe:
    print("The system is in a safe state.")
    print("Safe sequence:", ' -> '.join(f'P{p}' for p in safe_sequence))
else:
    print("The system is not in a safe state.")
