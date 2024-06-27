class MyQueue:
    def __init__(self) -> None:
        self._capacity = 4
        self._arr = []
        self._front_idx = 0
        self._rear_idx = 0

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
            self._rear_idx += 1

    def dequeue(self):
        if self._rear_idx == self._front_idx:
            raise ValueError("Queue is empty, can't dequeue")
        else:
            temp = self._arr.pop(0)
            self._rear_idx -= 1
            return temp
        
if __name__=='__main__':
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(20)
    queue.enqueue(3)
    print(queue)
    print(queue.dequeue())
    print(queue)