class FixedFirstEvictSecondQueue:
    def __init__(self):
        self._arr = []
        self._capacity = 3
    
    def __str__(self):
        return f'FixedFirstEvictSecondQueue({self._arr})'
    
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self._arr)
    
    def enqueue(self, item):
        if len(self._arr) >= self._capacity:
            self._arr.pop(1)  # Remove the second item (index 1)
        self._arr.append(item)
    
    def dequeue(self):
        if len(self._arr) == 0:
            raise ValueError("Queue is empty, can't dequeue")
        return self._arr.pop(1)
    
if __name__ == '__main__':
    queue = FixedFirstEvictSecondQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)  # Should print FixedFirstQueue([1, 2, 3])
    
    queue.enqueue(4)  # This should evict '2'
    print(queue)  # Should print FixedFirstQueue([1, 3, 4])
    
    queue.dequeue()  # Should remove '3'
    print(queue)  # Should print FixedFirstQueue([1, 4])
    
    queue.enqueue(5)  # This should evict '4'
    print(queue)  # Should print FixedFirstQueue([1, 5])