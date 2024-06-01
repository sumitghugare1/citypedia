def fifo_page_replacement(pages, capacity):
    page_faults = 0
    queue = []
    
    for page in pages:
        if page not in queue:
            if len(queue) == capacity:
                queue.pop(0)
            queue.append(page)
            page_faults += 1
        # Print the current state of the queue after each page request
        print(f"Page Request: {page}, Current Queue: {queue}")
    
    return page_faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4

print("\nRunning FIFO Page Replacement Algorithm:")
page_faults = fifo_page_replacement(pages, capacity)
print(f"\nTotal Page Faults: {page_faults}")
