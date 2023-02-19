class Stack:
    def __init__(self,maxSize):
        self.maxsize = maxSize
        self.list = []
        
    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        return False
    def push(self,value):
        if self.isFull():
            return 'Stack is Full'
        self.list.append(value)
        return 'Element has been successfully inserted'
    def peek(self):
        if self.isEmpty():
            return 'There is no elements'
        return self.list[len(self.list)-1]
    def delete(self):
        self.list = None
    
        
        
        
stack = Stack(4)
print(stack.isEmpty())
print(stack.isFull())
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack)