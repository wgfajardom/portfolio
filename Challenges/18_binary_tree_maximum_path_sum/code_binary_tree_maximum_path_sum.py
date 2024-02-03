### Challenge 18
### Binary Tree Maximum Path Sum



### Definition of auxiliary classes

# Class for a tree node
class Node:
    
    # Definition of Node
    def __init__(self, data, child_l=None, child_r=None):
        self.data = data
        self.child_l = child_l
        self.child_r = child_r

    # Representation of Node
    def __repr__(self):
        rep = "%s -> (%s, %s)" % (str(self.data), str(self.child_l), str(self.child_r))
        return rep


# Class for a tree
class Tree:
    
    # Definition of Tree
    def __init__(self, ls_data:list):
        if ls_data is None:
            root = Node(data=None)
        elif len(ls_data) == 1:
            root = Node(data=ls_data[0])
        else:
            root = Node(data=ls_data[0])
            nodes = [root]
        for i, x in enumerate(ls_data[1:]):
            if x is None:
                node = Node(data=None)
                nodes.append(node)
                continue
            parent_node = nodes[i // 2]
            is_left = (i % 2 == 0)
            node = Node(data=x)
            if is_left:
                parent_node.child_l = node
            else:
                parent_node.child_r = node
            nodes.append(node)
        self.root = root


    # Represent of Tree
    def __repr__(self):
        rep = Node.__repr__(self.root)
        return rep


    # Traverse Tree (pre-order traversal: parent -> leftChild -> rightChild)
    def preorderTraversal(self, node:Node):
        ret = []
        if node:
            ret.append(node.data)
            ret = ret + self.preorderTraversal(node.child_l)
            ret = ret + self.preorderTraversal(node.child_r)
        return ret
    

    # Get leafs (nodes without children) from a given node (subtree) in Tree
    def getLeafs(self, node):
        ret = []
        if node:
            aux_l = node.child_l
            aux_r = node.child_r
            if (aux_l is None) and (aux_r is None): 
                ret.append(node.data)
            ret = ret + self.getLeafs(node.child_l)
            ret = ret + self.getLeafs(node.child_r)
        return ret


    # Get all parent nodes from Tree
    def getAllParents(self, node:Node):
        ret = []
        if node:
            aux_l = node.child_l
            aux_r = node.child_r
            if (aux_l is not None) or (aux_r is not None): 
                ret.append(node)
            ret = ret + self.getAllParents(node.child_l)
            ret = ret + self.getAllParents(node.child_r)
        return ret


    # Get parent of node
    def getParent(self, node:Node, leaf:int|str):
        ret = None
        if node:
            aux_l = node.child_l
            aux_r = node.child_r
            if (aux_l is not None):
                if (aux_l.data == leaf):
                    ret = node.data
            if (aux_r is not None):
                if (aux_r.data == leaf):
                    ret = node.data
            if ret is None:
                ret = self.getParent(node.child_l, leaf)
            if ret is None:
                ret = self.getParent(node.child_r, leaf)
        return ret


    # Get all parents of a leaf, until reaching a specific target
    def fromLeafToTarget(self, node:Node, leaf:int|str, target:int|str):
        ret = [leaf]
        parent = self.getParent(node, leaf)
        if parent is not None:
            ret.append(parent)
            while parent != target:
                leaf = parent
                parent = self.getParent(node, leaf)
                ret.append(parent)
        return ret



### Definition of the class solution

class Solution18:

    # Validate input
    def check_input(self, root:list) -> bool:

        # Initialize validations
        # nn: the tree must have between 1 and 3*10^4 nodes
        # nv: nodes values should be between -1000 and 1000
        nn, nv = True, True

        # Perform validations
        clean_root = [elem for elem in root if elem != None]
        if (len(clean_root) < 1) or (len(clean_root) > 3e4):
            nn = False
        for elem in clean_root:
            if (float(elem) < -1000) or (float(elem) > 1000):
                nv = False

        return all([nn,nv])


    # Find path with maximum sum
    def maximum_path_sum(self, root:list) -> dict:

        # 1. Create a Tree from input and initialize variable to store complete paths
        t = Tree(ls_data=root)
        complete_paths = []
        
        # 2. Search all parent nodes in Tree and iterate over them. 
        # The reference parent node (par_node) will change with each iteration
        all_parent_nodes = t.getAllParents(node=t.root)
        for par_node in all_parent_nodes:

            # 2.A. Identify leaf nodes for left subtree
            l_subtree = par_node.child_l
            l_children = t.getLeafs(node=l_subtree)

            # 2.B. Find paths from leaf nodes of the left subtree to the reference parent node (par_node)
            dc_lch_path = dict()
            # Case when left subtree is not empty
            if len(l_children) > 0:
                for lch in l_children:
                    lch_path = t.fromLeafToTarget(node=t.root, leaf=lch, target=par_node.data)
                    dc_lch_path[lch] = lch_path
            # Case when left subtree is empty
            else:
                dc_lch_path["placeholder"] = []

            # 2.C. Identify leaf nodes for right subtree
            r_subtree = par_node.child_r
            r_children = t.getLeafs(node=r_subtree)

            # 2.D. Find paths from leaf nodes of the right subtree to the reference parent node (par_node)
            dc_rch_path = dict()
            # Case when right subtree is not empty
            if len(r_children) > 0:
                for rch in r_children:
                    rch_path = t.fromLeafToTarget(node=t.root, leaf=rch, target=par_node.data)
                    dc_rch_path[rch] = rch_path
            # Case when right subtree is empty
            else:
                dc_rch_path["placeholder"] = []

            # 2.E. Join paths from left and right subtrees
            for l_key in dc_lch_path.keys():
                for r_key in dc_rch_path.keys():
                    l_path = dc_lch_path[l_key]
                    r_path = dc_rch_path[r_key][::-1]
                    # When left subtree is non empty, remove the root node from paths of the right subtree to avoid repetition of the root node
                    if len(l_path) > 0:
                        r_path = r_path[1:]
                    aux_cp = l_path + r_path
                    complete_paths.append(aux_cp)

        # 3. Get all the possible paths
        # Recreate all possible subpaths from each complete path
        # Ex: if the complete path is [1,2,3,4]
        # All subpaths derived from it are [1,2,3,4] [1,2,3] [2,3,4] [1,2] [2,3] [3,4]
        all_paths = []
        for path in complete_paths:
            # Avoiding repetition of paths
            if (path not in all_paths) and (path[::-1] not in all_paths):
                all_paths.append(path)
            # Initiate parameters for sliding window
            k = len(path) - 1
            max_iter = 2
            # Identifying subpaths via an iterative sliding window
            # Iterations stop when sliding window size (k) is 1
            while k > 1:
                for ii in range(max_iter):
                    # Getting subpath
                    path_aux = path[ii:ii+k]
                    # Avoiding repetition of paths
                    if (path_aux not in all_paths) and (path_aux[::-1] not in all_paths):
                        all_paths.append(path_aux)
                # Recalculate parameters for sliding window
                k -= 1
                max_iter += 1

        # 4. Get the sum for all paths. Identify the maximum sum path.
        all_sum_paths = []
        maximum_sum_path = 0
        result_path = []
        for path in all_paths:
            aux_sum = sum(path)
            if aux_sum > maximum_sum_path:
                maximum_sum_path = aux_sum
                result_path = path
            all_sum_paths.append(aux_sum)
        dc_maximum_sum_path = {"all_paths": all_paths,
                               "all_sum_paths": all_sum_paths,
                               "maximum_path": result_path,
                               "maximum_sum": maximum_sum_path}

        return dc_maximum_sum_path


    # Get the maximum path sum in a Tree (main function)
    def main(self, root:list) -> dict:

        # Validation of inputs
        input_valid = self.check_input(self, root)

        # Case when input is valid
        if input_valid:

            # Retrieve the result
            dc_maximum_sum_path = self.maximum_path_sum(self, root)
            dc_result = {
                "input_valid": input_valid,
                "bst_as_list": root,
                "bst_as_tree": Tree(ls_data=root),
                "all_paths": dc_maximum_sum_path["all_paths"],
                "all_sum_paths": dc_maximum_sum_path["all_sum_paths"],
                "maximum_path": dc_maximum_sum_path["maximum_path"],
                "maximum_sum": dc_maximum_sum_path["maximum_sum"]
            }

        # Case when input is not valid
        else:
            # Retrieve the result
            dc_result = {
                "input_valid": input_valid,
                "bst_as_list": root
            }

        return dc_result
    


### Execution of the main function

# Initialize inputs
root1 = [1,2,3]
root2 = [-10,9,20,None,None,15,7]
root3 = [1,2,3,4,5,6,7,8,9,10,11,12]
root4 = [1,2,3,None,None,4,5,None,None,None,None,None,6,7]
root5 = [1,None,3,None,None,8]
root6 = []

# Executions
print("------------ Example 1 ------------")
dc_result_1 = Solution18.main(Solution18, root1)
print(dc_result_1)
print("------------ Example 2 ------------")
dc_result_2 = Solution18.main(Solution18, root2)
print(dc_result_2)
print("------------ Example 3 ------------")
dc_result_3 = Solution18.main(Solution18, root3)
print(dc_result_3)
print("------------ Example 4 ------------")
dc_result_4 = Solution18.main(Solution18, root4)
print(dc_result_4)
print("------------ Example 5 ------------")
dc_result_5 = Solution18.main(Solution18, root5)
print(dc_result_5)
print("------------ Example 6 ------------")
dc_result_6 = Solution18.main(Solution18, root6)
print(dc_result_6)