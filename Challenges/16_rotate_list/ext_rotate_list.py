### Challenge 16
### Rotate List
### External Solution


### Definition of auxiliary classes

# Class for the linked list node
class ListNode(object):

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

        
### Definition of the solution

# Class for the solution
class Solution:
    # Perform rotations
    def rotateRight(self, ll_head, k):
        
        if not ll_head:
            return ll_head
        
        # Connect tail to head
        cur = ll_head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1 
        cur.next = ll_head

        # Move to new head
        k = length - (k%length)
        while k > 0:
            cur = cur.next
            k -= 1

        # Disconnect and return new head
        newhead = cur.next
        cur.next=None
        
        return newhead
        
    # Function for i/o formatting     
    def io_format(self, head, k):
        
        # Formatting input (from list to ListNode)
        for ii in range(len(head)):
            if ii == 0:
                ln_head = ListNode(head[ii])
                aux = ln_head
            else:
                aux.next = ListNode(head[ii])
                aux = aux.next
        
        # Apply rotateRight function
        rot_ln_head = self.rotateRight(self, ln_head, k)
            
        # Format output
        output = []
        node = rot_ln_head
        while node is not None:
            output.append(node.data)
            node = node.next

        return output 
    


### Testing External Solution

# Initialize inputs
head1, k1 = [1,2,3,4,5], 2
head2, k2 = [0, 1, 2], 4
head3, k3 = [100, 200, 300], 2
head4, k4 = [1, 2, 3, 4, 5, 6, 7], 10

# Executions
print("------------ Example 1 ------------")
dc_result_1 = Solution.io_format(Solution, head1, k1)
print(dc_result_1)
print("------------ Example 2 ------------")
dc_result_2 = Solution.io_format(Solution, head2, k2)
print(dc_result_2)
print("------------ Example 3 ------------")
dc_result_3 = Solution.io_format(Solution, head3, k3)
print(dc_result_3)
print("------------ Example 4 ------------")
dc_result_4 = Solution.io_format(Solution, head4, k4)
print(dc_result_4)