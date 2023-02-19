class Queue:
    def __init__(self):
        self.items = []
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    def enqueue(self,value):
        self.items.append(value)
        return 'Element Inserted'
    def dequeue(self):
        if self.isEmpty():
            return 'The Queue is Empty'
        return self.items.pop(0)
    def peek(self):
        if self.isEmpty():
            return 'There is no elements in the Queue'
        return self.items[0]
    def delete(self):
        self.items = None