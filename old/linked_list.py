class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

    def search(self,data):
        temp = self.head
        while temp:
            if temp.data == data:
                print("True")
                return
            temp = temp.next
        print("False")
        return

    def search_by_index(self,index):
        if index < 0:
            print("Invalid Index")
            return
        
        temp,count = self.head,0
        while temp:
            if count == index:
                print(temp.data)
                return
            temp = temp.next
            count += 1
        print("Index not found")
        return 
        
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


    def insert_after(self,data,prev_val):
        temp = self.head
        while temp and temp.data != prev_val:
            temp = temp.next
        if not temp:
            print("Previous value not found")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def insert_before(self,data,before_val):
        if self.head is None:
            print("Empty List")
            return
        
        if self.head.data == before_val:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        
        prev = self.head
        temp = self.head.next

        while temp:
            if temp.data == before_val:
                new_node = Node(data)
                prev.next = new_node
                new_node.next = temp
                return
            prev = temp
            temp = temp.next

        print("Value not found in the list")


    def delete_by_value(self,key):
        if self.head is None:
            return
        
        if self.head.data == key:
            self.head = self.head.next
            return
        
        prev = self.head
        temp = self.head.next
        while temp:
            if temp.data == key:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        print("Value not found")

    def delete_by_index(self,index):
        if self.head is None:
            return

        if index < 0:
            print("Invalid Index")
            return

        if index == 0:
            self.head = self.head.next
            return

        temp =self.head
        count = 0

        while temp and count < index - 1:
            temp = temp.next
            count += 1

        if not temp or not temp.next:
            print("Index out of range")
            return

        temp.next = temp.next.next


ll = LinkedList()
ll.insert_at_start(34)
ll.insert_at_end(23)
ll.insert_at_end(53)
ll.traversal()
# ll.insert_at_end(53)
# ll.insert_before(314,53)
# ll.insert_before(314,53)
# ll.search(53)
# ll.search_by_index(6)
ll.traversal()

        
