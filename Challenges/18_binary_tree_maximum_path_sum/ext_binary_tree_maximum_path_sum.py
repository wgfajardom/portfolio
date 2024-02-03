### Challenge 18
### Binary Tree Maximum Path Sum
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

    # Get the maximum path sum from Tree (tree_root)
    def maxPathSum(self, tree_root:TreeNode) -> int:

        def dfs(node):
            # Base case: node is None
            if not node:
                return 0
            
            # Get the maximum sum of the left subtree
            left_sum = max(dfs(node.left), 0)
            # Get the maximum sum of the right subtree
            right_sum = max(dfs(node.right), 0)
            
            # Update the maximum path sum so far with the sum of the current node
            # and the maximum sums of the left and right subtrees
            self.max_path_sum = max(self.max_path_sum, node.val + left_sum + right_sum)
            
            # Return the maximum sum of the current node and the maximum sum of its
            # left and right subtrees
            return node.val + max(left_sum, right_sum)
        
        # Initialize the maximum path sum to negative infinity
        self.max_path_sum = float('-inf')
        
        # Start the depth-first search
        dfs(tree_root)
        
        # Return the maximum path sum
        return self.max_path_sum


    # Function for i/o formatting     
    def io_format(self, root:list):
        
        # Formatting input (from list to TreeNode)
        if len(root) > 0:
            root_node = TreeNode(val=root[0])
            nodes = [root_node]
            for i, x in enumerate(root[1:]):
                if x is None:
                    node = TreeNode(val=None)
                    nodes.append(node)
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
        result = self.maxPathSum(self, tree_root=root_node)
        
        # Format output
        return result



### Testing External Solution

# Initialize inputs
# Initialize inputs
root1 = [1,2,3]
root2 = [-10,9,20,None,None,15,7]
root3 = [1,2,3,4,5,6,7,8,9,10,11,12]
root4 = [1,2,3,None,None,4,5,None,None,None,None,None,6,7]
root5 = [1,None,3,None,None,8]
root6 = []

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
print("------------ Example 6 ------------")
result_6 = Solution.io_format(Solution, root6)
print(result_6)