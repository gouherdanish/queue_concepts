class FirstEvictQueue:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._arr = []

    def __str__(self) -> str:
        return f'FirstEvictQueue({self._arr})'

    def enqueue(self, item):
        if len(self._arr) >= self._capacity:
            self._arr.pop(0)  # Remove the oldest item
        self._arr.append(item)

    def dequeue(self):
        if len(self._arr) == 0:
            raise ValueError("Queue is empty, can't dequeue")
        return self._arr.pop(0)
    
if __name__ == '__main__':
    queue = FirstEvictQueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)  # Should print FirstEvictQueue([1, 2, 3])
    
    queue.enqueue(4)  # This should evict '1'
    print(queue)  # Should print FirstEvictQueue([2, 3, 4])
    
    queue.dequeue()  # Should remove '2'
    print(queue)  # Should print FirstEvictQueue([3, 4])
    
    queue.enqueue(5)  # This should evict '3'
    print(queue)  # Should print FirstEvictQueue([4, 5])