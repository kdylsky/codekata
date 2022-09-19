class Node:
    def __init__(self, value):
        self.val    = value
        self.next   = self.pre = None
  

class MyLinkedList():
    def __init__(self):        
        self.head   = None
        self.tail   = None
        self.count  = 0
    
    def print_all_from_head(self):
        if self.head == None:
            return None

        else:
            node = self.head
            while node != None:
                
                print(node.val)
                node = node.next  
        
        print("here")
        print(result)
    def print_all_from_tail(self):
        if self.tail == None:
            return None
        
        else:
            node = self.tail
            while node != None:
                print(node.val)
                node = node.pre

    def get(self, index):
        if self.head == None:
            return -1

        elif index > self.count -1:
            return -1 
        
        else:
            node = self.head
            for _ in range(index):
                node = node.next
            
            return node.val 
         

    def addAtHead(self, val):
        if self.head == None:
            self.head   = Node(val)
            self.tail   = self.head
            self.count += 1
        
        else:
            curr_head           = self.head
            new_head            = Node(val)
            new_head.next       = curr_head
            new_head.next.pre   = new_head
            self.head           = new_head
            self.count         += 1
    
    def addAtTail(self, val):
        if self.head == None:
            self.head   = Node(val)
            self.tail   = self.head
            self.count += 1
        
        else:
            curr_head                = self.head
            
            while curr_head.next    != None:
                curr_head            = curr_head.next
            
            curr_head.next  = Node(val)
            self.tail       = curr_head.next
            self.tail.pre   = curr_head
            self.count      += 1

    def addAtIndex(self, index, val):
        if self.head == None or self.count < index:
            return None
        
        elif self.count == index:
            curr_head = self.head
            
            while curr_head.next != None:
                curr_head = curr_head.next
            
            curr_head.next  = Node(val)
            self.tail       = curr_head.next
            self.tail.pre   = curr_head

            self.count      += 1
        
        elif index == 0:
            curr_head           = self.head
            new_head            = Node(val)
            new_head.next       = curr_head
            new_head.next.pre   = new_head
            self.head           = new_head
            self.count          += 1

        else:
            node = self.head
            
            for _ in range(index-1):
                node = node.next
            
            temp_node       = node.next
            node.next       = Node(val)
            temp_node.pre   = node.next
            node.next.pre   = node
            node.next.next  = temp_node 
            self.count      += 1
    
    def deleteAtIndex(self, index):
        if self.head == None:
            return None
        
        elif index > self.count-1:
            return None
        
        elif index == 0:
            node            = self.head
            new_head        = node.next
            node.next.pre   = None
            self.head       = new_head
            self.count      -= 1

            return "ok"
            
        elif index == self.count -1:
            node            = self.tail
            new_tail        = node.pre
            new_tail.next   = None
            node.pre        = None
            self.tail       = new_tail
            self.count      -= 1
            
            return "ok"
        
        else:
            node = self.head
            
            for _ in range(index):
                node        = node.next
            
            temp_pre        = node.pre
            temp_next       = node.next

            temp_pre.next   = temp_next
            temp_next.pre   = temp_pre
            self.count      -= 1

            return "ok"


test = MyLinkedList()

test.addAtTail(10)
test.addAtTail(20)
test.addAtTail(30)
test.addAtTail(40)

test.print_all_from_head()


# print("head부터 출력")
# test.print_all_from_head()
# print("tail부터 출력")
# test.print_all_from_tail()


# print("===========")
# print(test.get(10))


# print(test.count)
# print("=============here")
# print(test.deleteAtIndex(3))
# print("=============here")

# print("head부터 출력")
# test.print_all_from_head()
# print("tail부터 출력")
# test.print_all_from_tail()

# print(test.count)