class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
        
        
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node=node.next
    def create(self,nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'DLL is created'
    def insert(self,nodeValue,location):
        if self.head is None:
           return 'Node Cannot be inserted'
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.prev = newNode
                tempNode.next = newNode
    def tansverse(self):
        if self.head is None:
            return 'There is no elements to transverse'
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    def reverse(self):
        if self.head is None:
            return 'There is no elements to get'
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    def search(self,nodeValue):
        if self.head is None:
            return "There is no Nodes in this DLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return 'The node does not exist in this list'
    def remove(self,location):
        if self.head is None:
          return 'DLL does not exist'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head == self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    
            else:
                
                curNode = self.head
                index = 0
                while index > location-1:
                    curNode = curNode.next
                    index +=1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
                
        def delete(self):
            self.head = None
            self.tail = None
                    
                        
                
                    
                    
                    
        
                
                
                
                