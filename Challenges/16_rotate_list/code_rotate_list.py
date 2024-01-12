### Challenge 16
### Rotate List



### Definition of auxiliary classes

# Class for a node
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


# Class for a Linked List
class LinkedList:

    # Definition of Linked List
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes[0])
            self.head = node
            for elem in nodes[1:]:
                node.next = Node(data=elem)
                node = node.next

    # Representation of Linked List
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Iteration of nodes from Linked List
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    # Length of Linked List
    def length(self) -> int:
        size = 0
        cur = self.head
        while cur is not None:
            size += 1
            cur = cur.next
        return size

    # Find specific node from Linked List based on its position
    def find(self, n: int) -> Node:
        count = 1
        cur = self.head
        while count != n:
            cur = cur.next
            count += 1
        return cur

    # Add node at the beginning of the Linked List
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # Remove node from Linked List
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)



### Definition of the class solution

class Solution16:

    # Validate input
    def check_input(self, head: list, k: int) -> bool:

        # Initialize validations
        # hl: head length should be less than 501
        # hv: nodes of head should be between -100 and 100
        # kv: k should be between 0 and 2*10^9
        hl, hv, kv = True, True, True

        # Perform validations
        if (len(head) < 1) or (len(head) > 500):
            hl = False
        for elem in head:
            if (elem < -100) or (elem > 100):
                hv = False
        if (k < 0) or (k > 2*10e9):
            kv = False

        return all([hl, hv, kv])


    # Perform k rotations to the right
    def rotateRight(self, head: list, k: int) -> LinkedList:

        # Convert input from list to LinkedList
        ll_head = LinkedList(head)

        # Define number of rotations
        ll_len = ll_head.length()
        num_rot = k%ll_len

        # Rotations
        for ii in range(num_rot):
            # Find node to move from tail to head
            node2move = ll_head.find(n=ll_len)
            # Remove node from tail
            ll_head.remove_node(node2move.data)
            # Add node to head
            ll_head.add_first(node2move)

        # Formatting output from LinkedList to list
        output = []
        node = ll_head.head
        while node is not None:
            output.append(node.data)
            node = node.next

        return output 


    # Rotation of a Linked List (main function)
    def main(self, head:list, k:int):

        # Validation of inputs
        input_valid = self.check_input(self, head, k)

        # Case when input is valid
        if input_valid:

            # Retrieve the result
            head_res = self.rotateRight(self, head, k)
            dc_result = {
                "input_valid": input_valid,
                "input_head": head,
                "input_k": k,
                "output_head": head_res
            }

        # Case when input is not valid
        else:
            # Retrieve the result
            dc_result = {
                "input_valid": input_valid,
                "input_head": head,
                "input_k": k,
            }

        return dc_result



### Execution of the main function

# Initialize inputs
head1, k1 = [1,2,3,4,5], 2
head2, k2 = [0, 1, 2], 4
head3, k3 = [100, 200, 300], 2
head4, k4 = [1, 2, 3, 4, 5, 6, 7], 10

# Executions
print("------------ Example 1 ------------")
dc_result_1 = Solution16.main(Solution16, head1, k1)
print(dc_result_1)
print("------------ Example 2 ------------")
dc_result_2 = Solution16.main(Solution16, head2, k2)
print(dc_result_2)
print("------------ Example 3 ------------")
dc_result_3 = Solution16.main(Solution16, head3, k3)
print(dc_result_3)
print("------------ Example 4 ------------")
dc_result_4 = Solution16.main(Solution16, head4, k4)
print(dc_result_4)