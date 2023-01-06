class Solution:
    def rotate_linked_list_upto_kth_times(self, head, k):
        # print("reverse func > ", head.data)
        current = head
        count = 0
        kthNode = head
        nextHead = head

        while current.next != None:
            count += 1
            if count == k:
                kthNode = current
                nextHead = current.next
            current = current.next

        if count != k - 1:
            current.next = head
            head = nextHead
            kthNode.next = None

        return head

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        node = Node(new_data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = node

    def push_left(self, new_data):
        node = Node(new_data)
        if self.head == None:
            self.head = node
            return

        node.next = self.head
        self.head = node
 
    # Utility function to print the LinkedList
    def print_list(self):
        current = self.head
        while current:
            print(str(current.data) + " --> ", end="")
            current = current.next
        print("None")

    def print_list_by_head(self, head):
        current = head
        while current:
            print(str(current.data) + " --> ", end="")
            current = current.next
        print("None")

# Driver code
ll = LinkedList()

# ll.push(2)
# ll.push(4)
# ll.push(7)
# ll.push(8)
# ll.push(9)

ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.push(7)
ll.push(8)

# ll.push_left(20)
# ll.push_left(4)
# ll.push_left(15)
# ll.push_left(85)

ll.print_list()
# print(ll.head.data)

obj = Solution()
k = 4
new_head = obj.rotate_linked_list_upto_kth_times(ll.head, k)
ll.print_list_by_head(new_head)


# here we need to rotate a linked list.
# we already have "k", which denotes the number of times we need to rotate or the number of nodes we need to pass before making the linked list rotate.
# so after generating the linked list we are calling our Solution class function to rotate this.
# the process to do this is following -.
# 1. we take a counter variable which will be increased omn each iteration and whenever it matches with the "k", we will store few data.
# 2. we need to store the kth-Node and Next of the k-th Node.
# 3. because we need to point kth-Node next to None or Null, we need to point our last node next to the head and we need to change the head to the Next of the k-th Node.


# here time complexity of the solution will be - O(n) and space complexity will be - O(1).
# as we are iterating, the time is directly dependent upon the size of the linked list. So the time complexity will be O(n).
# as we are using variables to store kth node, next of the kth node and count which are constant and not directly dependent on the size of the linked list, the space complexity will be O(1).

# Video Link - https://www.youtube.com/watch?v=tWtq2nd7sI4
