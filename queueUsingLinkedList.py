class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'Node({self.val})'
    
    def __repr__(self) -> str:
        return str(self)

class SLL:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0
    
    def __str__(self) -> str:
        return ','.join([str(node.val) for node in self])
    
    def __iter__(self):
        curr = self._head
        while curr:
            yield curr
            curr = curr.next

    def __len__(self):
        return self._length

    def isEmpty(self):
        """
        O(1)
        """
        return self._head is None
    
    def insert(self,new_val):
        """
        O(1)
        """
        new_node = ListNode(new_val)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1

    def delete(self):
        """
        O(1)
        """
        if self._head is None:
            raise ValueError("Popping from an empty queue")
        else:
            temp = self._head
            if self._length == 1:
                self._head = None
                self._tail = None
            else:
                self._head = self._head.next
                temp.next = None
            return temp.val
    
        
class MyQueue:
    def __init__(self) -> None:
        self._sll = SLL()
    
    def __str__(self) -> str:
        return f'MyQueue({self._sll})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __len__(self):
        return len(self._sll)
    
    def enqueue(self,new_val):
        self._sll.insert(new_val)

    def dequeue(self):
        return self._sll.delete()
    
    
if __name__=='__main__':
    queue = MyQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    print(queue.dequeue())
    print(queue)
            
    