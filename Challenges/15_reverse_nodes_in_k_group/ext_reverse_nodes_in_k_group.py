### Challenge 15
### Reverse Nodes in k-Group
### External Solution


### Definition of the solution

# Class for the linked list nodes
class ListNode(object):

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


# Class for the solution
class Solution:
    
    # Reverse operation for each k-group
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # Edge cases
        if not head or not head.next or k == 1: 
            return head

        dummy = ListNode(-1, head)
        groupPrev = dummy
        while True:
            # Get kth node of the group
            kth = self.getKth(self, groupPrev, k)
            if not kth: 
                break
            groupNext = kth.next

            # Reverse Group
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                curr.next, prev, curr = prev, curr, curr.next

            # Move groupPrev pointer to the next group position (node before next group)
            groupPrev.next, groupPrev = kth, groupPrev.next

        return dummy.next

    # Get the kth node of the group
    def getKth(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    # Function for i/o formatting
    def io_format(self, head: ListNode, k: int) -> list: 

        # Formatting input (from list to ListNode)
        for ii in range(len(head)):
            if ii == 0:
                ln_head = ListNode(head[ii])
                aux = ln_head
            else:
                aux.next = ListNode(head[ii])
                aux = aux.next
        
        # Apply Solution class
        result = Solution.reverseKGroup(Solution, ln_head, k)
        
        # Formatting output (from ListNode to list)
        output = []
        while result:
            output.append(result.data)
            result = result.next
        return output



### Testing External Solution

# Initialize inputs
head1, k1 = [1,2,3,4,5], 2
head2, k2 = [1,2,3,4,5], 3
head3, k3 = [1,2,3,4,5,6,7,8,9], 3
head4, k4 = [1,2,3,4,5,6,7], 9

# Executions
print("------------ Example 1 ------------")
output1 = Solution.io_format(Solution, head1, k1)
print(head1, k1)
print(output1)
print("------------ Example 2 ------------")
output2 = Solution.io_format(Solution, head2, k2)
print(head2, k2)
print(output2)
print("------------ Example 3 ------------")
output3 = Solution.io_format(Solution, head3, k3)
print(head3, k3)
print(output3)
print("------------ Example 4 ------------")
output4 = Solution.io_format(Solution, head4, k4)
print(head4, k4)
print(output4)