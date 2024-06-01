import random
import time

# Shared buffer and buffer size
buffer = []
BUFFER_SIZE = 5

def produce():
    return random.randint(1, 100)

def producer():
    item = produce()
    if len(buffer) < BUFFER_SIZE:
        buffer.append(item)
        print(f'Produced {item}')
    else:
        print('Buffer full, producer is waiting')
def consumer():
    if buffer:
        item = buffer.pop(0)
        print(f'Consumed {item}')
    else:
        print('Buffer empty, consumer is waiting')
# Simulate producer and consumer
for _ in range(10):
    producer()
    time.sleep(0.5)  # Simulate time delay for producing
    consumer()
    time.sleep(0.5)  # Simulate time delay for consuming
