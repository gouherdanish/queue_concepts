class MyQueue:
    def __init__(self) -> None:
        self._capacity = 4
        self._arr = [None]*self._capacity
        self._head_idx = 0
        self._tail_idx = 0

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
        if self._tail_idx == self._head_idx:
            raise ValueError("Queue is empty, can't dequeue")
        else:
            temp = self._arr[self._head_idx]
            self._arr[self._head_idx] = None
            self._head_idx += 1
            return temp
        
if __name__=='__main__':
    q = MyQueue()
    q.enqueue(1)
    print(q)