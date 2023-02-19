class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self,val):
        self.list.append(val)
        return 'Element added successfully inserted'
    def pop(self):
        if self.isEmpty():
            return 'List is empty'
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return 'Empty list'
        
        return self.list(len(self.list)-1)
    def delete(self):
        self.list = None
    
            
    