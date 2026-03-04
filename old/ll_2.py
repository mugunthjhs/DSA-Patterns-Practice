class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_all_items(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

    def search_by_value(self,value):
        temp = self.head
        while temp:
            if temp.data == value:
                print("True")
                return
            temp = temp.next
        print("False")
        return
    
    def search_by_index(self,index):
        if 0 > index:
            print("Invalid Index")
            return
        temp = self.head
        count = 0
        while temp:
            if count == index:
                print(f"Index {index} value is: {temp.data}")
                return
            temp = temp.next
            count +=1
        print("Index not found")

    def delete_by_value(self,value):
        if self.head is None:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        prev = self.head
        temp = self.head.next
        while temp:
            if temp.data == value:
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
        prev = self.head
        temp = self.head.next
        count = 0
        while temp:
            if count == index - 1:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
            count += 1

        print("Index out of range")
        
    def insert_after(self,prev_val,data):
        temp = self.head

        while temp and temp.data != prev_val:
            temp = temp.next

        if not temp:
            print("No previous value found")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        
    def reverse(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        print(f"Length of nodes: {count}")

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print(f"Middle Element: {slow.data}")

    def find_nth_from_last(self,n):
        first = self.head #22
        second = self.head

        for _ in range(n):
            if not first:
                print("List shorter than",n)
                return
            first = first.next

        while first:
            first = first.next 
            second = second.next

        print(f"The nth from last is: {second.data}")



ll = LinkedList()
ll.insert_at_beginning(232)
ll.insert_at_beginning(29)
ll.insert_at_beginning(11)
ll.insert_at_beginning(33)
ll.insert_at_end(783)

ll.insert_after(3,777)
ll.print_all_items()
ll.reverse()
ll.find_middle()
ll.find_nth_from_last(3)
ll.print_all_items()
ll.length()