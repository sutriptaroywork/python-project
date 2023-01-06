class Solution:
    def remove_a_loop_in_linked_list(self, head):
        if head == None or head.next == None:
            return
        
        slow, fast = head.next, head.next.next
        
        while fast and fast.next != None:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
            
        if slow == fast:
            
            slow = head
            
            if slow == fast:
                while fast.next != slow:
                    fast = fast.next
            else:
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next

            fast.next = None

#{ 
# Driver Code Starts
# driver code:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next

    def isLoop(self):
        if self.head is None:
            return False
        
        fast=self.head.next
        slow=self.head
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
        
        return True
    
    def loopHere(self,position):
        if position==0:
            return
        
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk

    def length(self):
        walk=self.head
        ret=0
        while walk:
            ret+=1
            walk=walk.next
        return ret

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        Solution().remove_a_loop_in_linked_list(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)

# } Driver Code Ends


# here we need to remove loop from a linked list.
# so to do that, we need to follow 3 steps.
# 1. detect that the linked has an loop or not.
# 2. detect the node on which it is looping.
# 3. point the next of the previous node of that node as "None" or "NULL".


# here time complexity of the solution will be - O(n) and space complexity will be - O(1).
# as we are iterating, the time is directly dependent upon the size of the linked list. So the time complexity will be O(n).
# as we are using variables to store data which is not directly dependent on the size of the linked list, the space complexity will be O(1).

# Video Link - https://www.youtube.com/watch?v=jcZtMh_jov0 / https://www.youtube.com/watch?v=qsPoOVAHV_I / https://www.youtube.com/watch?v=VxOFflTXlXo / 
