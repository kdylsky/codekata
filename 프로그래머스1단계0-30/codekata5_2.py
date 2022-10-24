class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.prev = None

class MyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def get(self, index):
        if index >= self.count:
            return -1

        node = self.head
        counting = 0
        while counting < index:
            node = node.next
            counting += 1
        return node.val


    def addAtHead(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
            self.count += 1
        else: 
            cur_head = self.head
            cur_head.prev = Node(val)
            self.head = cur_head.prev
            self.head.next = cur_head
            self.count += 1


    def addAtTail(self, val):
        if self.tail == None:
            self.tail = Node(val)
            self.head = self.tail
            self.count += 1
        else:
            node = self.tail
            node.next = Node(val)
            self.tail = node.next
            self.tail.prev = node
            self.count += 1
        
    def addAtIndex(self, index, val):
        node = self.head
        if index == self.count:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index > self.count:
            return
        else:
            count = 0
            while count < index:
                node = node.next
                count += 1
            new_node = Node(val)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
            self.count += 1

    def deleteAtIndex(self, index):
        if index >= self.count:
            return "invalid_index"
        elif index == self.count-1:
            self.tail = self.tail.prev
            self.tail.next = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            node = self.head
            counting = 0
            while counting < index:
                node = node.next
                counting += 1
            node.prev.next = node.next
            node.next.prev = node.prev
        self.count -= 1


    def print_linked(self):
        self = self.head
        while self != None:
            print(self.val)
            self = self.next



