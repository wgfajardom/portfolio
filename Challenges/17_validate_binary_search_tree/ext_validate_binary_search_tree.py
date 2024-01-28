### Challenge 17
### Validate Binary Search Tree
### External Solution



### Definition of auxiliary classes

# Class for the tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


### Definition of the solution

# Class for the solution
class Solution:    
    
    # Start recursion
    def isValidBST(self, root_node:TreeNode) -> bool:
        
        # Start the recursive checking with initial minimum and maximum values as -infinity and +infinity
        return self.is_valid_bst_helper(self, root_node, float('-inf'), float('inf'))

    
    # Recursive calls
    def is_valid_bst_helper(self, node, min_val, max_val):

        if not node:
            return True
            
        # Check if the current node's value is within the valid range
        if not (min_val < node.val < max_val):
            return False
            
        # Check left subtree with updated max_val
        left_valid = self.is_valid_bst_helper(self, node.left, min_val, node.val)
        # Check right subtree with updated min_val
        right_valid = self.is_valid_bst_helper(self, node.right, node.val, max_val)
        
        # Both subtrees must be valid BSTs for the whole tree to be a valid BST
        return left_valid and right_valid


    # Function for i/o formatting     
    def io_format(self, root:list):
        
        # Formatting input (from list to TreeNode)
        if len(root) > 0:
            root_node = TreeNode(val=root[0])
            nodes = [root_node]
            for i, x in enumerate(root[1:]):
                if x is None:
                    continue
                parent_node = nodes[i // 2]
                is_left = (i % 2 == 0)
                node = TreeNode(val=x)
                if is_left:
                    parent_node.left = node
                else:
                    parent_node.right = node
                nodes.append(node)
        else:
            return TreeNode(val=None)
    
        # Apply isValidBST function
        result = self.isValidBST(self, root_node)
        
        # Format output
        return result



### Testing External Solution

# Initialize inputs
root1 = [2,1,3]
root2 = [5,1,4,None,None,3,6]
root3 = []
root4 = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
root5 = [9,6,11,4,None,8,10,None,None,None,None,5]

# Executions
print("------------ Example 1 ------------")
result_1 = Solution.io_format(Solution, root1)
print(result_1)
print("------------ Example 2 ------------")
result_2 = Solution.io_format(Solution, root2)
print(result_2)
print("------------ Example 3 ------------")
result_3 = Solution.io_format(Solution, root3)
print(result_3)
print("------------ Example 4 ------------")
result_4 = Solution.io_format(Solution, root4)
print(result_4)
print("------------ Example 5 ------------")
result_5 = Solution.io_format(Solution, root5)
print(result_5)