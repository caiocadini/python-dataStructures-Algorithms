from Node import Node  # Assuming Node is correctly implemented in Node.py
from Queue import Queue  # Assuming Queue is in a file named Queue.py

def test_queue():
    print("Testing Queue Implementation")

    # Create a new Queue instance
    queue = Queue()

    # Test isEmpty on an empty queue
    print("Is the queue empty?", queue.isEmpty())  # Expected: True

    # Test enqueue
    print("\nEnqueuing elements 1, 2, 3")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Print the queue
    print("\nQueue after enqueuing 1, 2, 3:")
    queue.printQueue()  # Expected: 1 2 3

    # Test size
    print("\nCurrent size of the queue:", queue.size)  # Expected: 3

    # Test isEmpty on a non-empty queue
    print("Is the queue empty?", queue.isEmpty())  # Expected: False

    # Test dequeue
    print("\nDequeuing an element:", queue.dequeue().data)  # Expected: 1

    # Print the queue after dequeue
    print("\nQueue after dequeuing one element:")
    queue.printQueue()  # Expected: 2 3

    # Test clear
    print("\nClearing the queue:")
    queue.clear()  # Expected: removes all elements and prints them

    # Print the queue after clear
    print("\nQueue after clearing:")
    queue.printQueue()  # Expected: (nothing should be printed)

    # Test isEmpty after clear
    print("Is the queue empty?", queue.isEmpty())  # Expected: True

    # Test size after clear
    print("Current size of the queue:", queue.size)  # Expected: 0

if __name__ == "__main__":
    test_queue()
