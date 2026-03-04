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
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")
    
    def find_duplicate_sorted(self):
        curr = self.head

        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next

    def find_duplicates_unsorted(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def find_middle(self):
        if self.head is None:
            return None    
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(f"middle: {slow.data}")
        
    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        self.head = prev

            


ll = LinkedList()
ll.insert_at_beginning(322)
ll.insert_at_beginning(322)
ll.insert_at_beginning(322)
ll.insert_at_beginning(41)
ll.insert_at_beginning(41)
ll.insert_at_beginning(414522)
ll.insert_at_beginning(41)
ll.insert_at_beginning(424)
ll.insert_at_beginning(424)
ll.insert_at_beginning(13)

ll.find_middle()
ll.print_all_items()
ll.reverse()
ll.print_all_items()