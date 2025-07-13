class MyQueue:
    def __init__(self) -> None:
        self._capacity = 2
        self._arr = []

    def __str__(self) -> str:
        return f'MyQueue({self._arr})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __len__(self):
        return len(self._arr)

    def enqueue(self,item):
        if len(self._arr) >= self._capacity:
            raise OverflowError("Queue is full, can't enqueue")
        else:
            self._arr.append(item)

    def dequeue(self):
        if len(self._arr) == 0:
            raise ValueError("Queue is empty, can't dequeue")
        else:
            temp = self._arr.pop(0)
            return temp
        
if __name__=='__main__':
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(20)
    queue.enqueue(3)
    print(queue, len(queue))
    print(queue.dequeue())
    print(queue, len(queue))
    queue.enqueue(4)
    print(queue, len(queue))