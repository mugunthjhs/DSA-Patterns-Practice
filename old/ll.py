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
    
    def print_all_items(self):
        temp = self.head
        while temp and temp.data:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self,value):
        if self.head is None:
            return

        if self.head == value:
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


    def insert_after(self,data,prev_value):
        temp = self.head
        while temp and temp.data != prev_value:
            temp = temp.next
        
        if temp is None:
            print("Value not found")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        
    def insert_before(self,data,before_value):
        new_node = Node(data)
        if self.head.data == before_value:
            new_node.next = self.head
            self.head = new_node
            return    
        prev = self.head
        temp = self.head.next

        while temp and temp.data != before_value:
            prev = temp
            temp =temp.next 
        if temp is None:
            print("value not found")
        prev.next = new_node
        new_node.next = temp


    def delete_by_value(self,value):
        if self.head is None:
            print("Empty List")
            return
        if self.head.data == value:
            self.head = self.next
            return
     
        prev = self.head
        temp = self.head.next
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        
    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print("Count:",count)
             
    # list = [A , B , C]

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow:
            print("Middle Element:",slow.data)

    
    def find_loop(self):
        slow = self.head
        fast = self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Loop detected")
                return True
        print("No Loop")
        return False

        

ll = LinkedList()
ll.delete_by_value(25)
ll.print_all_items()
ll.insert_at_beginning(34)
ll.insert_at_beginning(2425)
ll.insert_at_beginning(25)
ll.insert_at_beginning(2425)
ll.insert_at_end(1331)
ll.delete_by_value(34)
ll.insert_after(5242452,25)
ll.insert_before(9773,25)
ll.insert_before(9,9773)
ll.length()
ll.print_all_items()
ll.reverse()
ll.print_all_items()
ll.find_loop()
ll.find_middle()