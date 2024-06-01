def first_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    return allocation

# Example data
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

# Run the First Fit algorithm
allocation = first_fit(blocks, processes)

# Print the results
print("Process No.  Process Size  Block No.")
for i in range(len(processes)):
    print(f"{i + 1}            {processes[i]}            {allocation[i] + 1 if allocation[i] != -1 else 'Not Allocated'}")

