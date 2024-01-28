### Challenge 17
### Validate Binary Search Tree



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
    def __init__(self, nodes=None|list):

        # Trivial definition
        self.root = Node(None)
        self.deps = None
        self.pars = None
        self.hist = None
        self.nodes = None

        #### Definition from list of nodes
        if (nodes is not None):

            ### Tree root
            self.root = Node(nodes[0])

            ### Identify nodes properties
            # dep: node depth (1,2,3,...)
            # dir: node direction from parent perspective, left ("l") or right ("r")
            # par: indicator of parent location (index + 1)
            # his: consecutive directions from root to node
            ls_deps, ls_dirs, ls_pars, ls_hist = [1], ["-"], [0], [["-"]]

            ### Find properties of each node
            for aux_count in range(2,len(nodes)+1):
                
                ## Find dep, dir, par
                dep = len(bin(aux_count))-2
                dir = "l" if aux_count%2 == 0 else "r"
                par = int(aux_count/2)
                ls_deps.append(dep)
                ls_dirs.append(dir)
                ls_pars.append(par)

                ## Find his                
                # Instantiate parent node location (par) and node history (his) before iterating to the root
                idx = aux_count-1
                par = ls_pars[idx]
                his = []
                # Iterate over parent nodes until reaching the root
                while par != 0:
                    # Add dir from previous parent node to his 
                    dir = ls_dirs[idx]
                    his = [dir] + his
                    # Recalculate previous parent node location for next iteration
                    idx = par-1
                    par = ls_pars[idx]
                # Save his
                ls_hist.append(his)

            ### Build tree from nodes properties
                
            ## Identify how many parent nodes are
            max_dep = max(ls_deps)
            range_parnts = len([elem for elem in ls_deps if elem < max_dep])

            ## Build tree by iterating over all parent nodes
            for ii in range(range_parnts):

                # Retrieve children properties
                # ls_chs: list of children nodes
                # ls_his: list of children history (consecutive directions from root to node)
                par_id = ii+1
                ls_chs = [nodes[ii] for ii in range(len(nodes)) if ls_pars[ii] == par_id]
                ls_his = [ls_hist[ii] for ii in range(len(nodes)) if ls_pars[ii] == par_id] 

                # Assign children nodes
                if (len(ls_chs) == 2):
                    self.add_child(node=Node(ls_chs[0]), directions=ls_his[0], init=True)
                    self.add_child(node=Node(ls_chs[1]), directions=ls_his[1], init=True)
                if len(ls_chs) == 1:
                    self.add_child(node=Node(ls_chs[0]), directions=ls_his[0], init=True)

            ### Save nodes properties
            self.deps = ls_deps
            self.pars = ls_pars
            self.hist = ls_hist
            self.nodes = nodes


    # Representation of Tree
    def __repr__(self):       
        return self.root.__repr__()


    # Move through Tree starting from the root 
    def move(self, directions:list):
        # Starting point is the root
        t_aux = self.root
        for dir in directions:
            # Move to left
            if dir == "l":
                t_aux = t_aux.child_l
            # Move to right
            elif dir == "r":
                t_aux = t_aux.child_r
            # Do not move
            else:
                t_aux = t_aux
        return t_aux


    # Add child node to Tree
    def add_child(self, node:Node, directions:list, init:bool=False):

        # Locate parent node
        t_aux = self.move(directions[:-1])
        # Direction of child node
        dir = directions[-1]
        # Adding child node to parent node
        if node.data is not None:
            if dir == "l":
                t_aux.child_l = node
            else:
                t_aux.child_r = node

        # Setting node properties when a single node is added (not via __init__)
        if init == False:

            # Reproduce aux_count from directions
            aux_count = 1
            power = 1
            for dir in directions[::-1]:
                if dir == "l":
                    aux_count += 1**(power)
                elif dir == "r":
                    aux_count += 2**(power)
                else:
                    aux_count += 0
                power += 1

            # Identifying position of new nodes based on a masking method
            ln = len(self.nodes)
            len_nodes = (2**power)-1
            mask_nodes = [1 if ii+1 <= ln else 0 for ii in range(len_nodes)]
            mask_nodes[aux_count-1] = 2
            
            # Populating deps, pars, hist, and nodes
            nodes, deps, pars, hist = [], [], [], []
            for ii in range(len_nodes):
                aux_count = ii + 1
                # Masking = 1 -> Node already exists in the Tree
                if mask_nodes[ii] == 1:
                    deps.append(self.deps[ii])
                    pars.append(self.pars[ii])
                    hist.append(self.hist[ii])
                    nodes.append(self.nodes[ii])
                # Masking = 2 -> Node recently added to the Tree via add_child
                elif mask_nodes[ii] == 2:
                    deps.append(len(bin(aux_count))-2)
                    pars.append(int(aux_count/2))
                    hist.append(directions)
                    nodes.append(node.data)
                # Masking = 0 -> None node must be added to preserve lists length of deps, pars, hist, and nodes
                else:
                    deps.append(len(bin(aux_count))-2)
                    pars.append(int(aux_count/2))
                    hist.append([*str(bin(aux_count))[3:].replace("0","l").replace("1","r")])
                    nodes.append(None)

            # Update deps, pars, hist, and nodes as attributes of Tree
            self.deps = deps
            self.pars = pars
            self.hist = hist
            self.nodes = nodes


    # Traverse Tree (pre-order traversal)
    def traverse(self, node:Node):
       ret = []
       if node:
           ret.append(node.data)
           ret = ret + self.traverse(node.child_l)
           ret = ret + self.traverse(node.child_r)
       return ret



### Definition of the class solution

class Solution17:

    # Validate input
    def check_input(self, root:list) -> bool:

        # Initialize validations
        # nn: the tree must have between 1 and 10^4 nodes
        # nv: nodes values should be between -2^31 and 2^31 - 1
        nn, nv = True, True

        # Perform validations
        clean_root = [elem for elem in root if elem != None]
        if (len(clean_root) < 1) or (len(clean_root) > 1e4):
            nn = False
        for elem in clean_root:
            if (float(elem) < -2e31) or (float(elem) > 2e31):
                nv = False

        return all([nn,nv])


    # Binary search tree validation by node
    def bst_validation(self, root:list) -> dict:

        # Create a Tree from input
        t = Tree(nodes=root)

        # Identify parent nodes
        max_dep = max(t.deps)
        range_parnts = len([elem for elem in t.deps if elem < max_dep])

        # Initialize variables where result will be stored
        dc_validations = dict()
        valid_bst = True
        count = 0

        # Iterate over all parent nodes
        for his in t.hist[0:range_parnts]:

            # Locate on current parent node
            t_aux = t.move(his)

            # Left sub-branch validation: verify if left sub-branch of current node is a BST
            lsbv = True
            if (t_aux is not None) and (t_aux.child_l is not None):
                if t_aux.child_l.data < t_aux.data:
                    children = t.traverse(node=t_aux.child_l)
                    if children != []:
                        children_validation = [ch for ch in children if (t_aux.data - ch) > 0]
                        if len(children_validation) != len(children):
                            lsbv = False
                else:
                    lsbv = False

            # Right sub-branch validation: verify if right sub-branch of current node is a BST
            rsbv = True
            if (t_aux is not None) and (t_aux.child_r is not None):
                if t_aux.child_r.data > t_aux.data:
                    children = t.traverse(node=t_aux.child_r)
                    if children != []:
                        children_validation = [ch for ch in children if (t_aux.data - ch) < 0]
                        if len(children_validation) != len(children):
                            rsbv = False
                else:
                    rsbv = False
            
            # Store results by node
            if t_aux is None: count += 1
            key = t_aux.data if t_aux is not None  else "NullNode"+str(count)
            value = [lsbv, rsbv]
            dc_validations[key] = value

        # Store overall results
        for value in dc_validations.values():
            if all(value) == False:
                valid_bst = False
        dc_validations["result"] = valid_bst

        return dc_validations


    # Binary search tree validation (main function)
    def main(self, root:list) -> dict:

        # Validation of inputs
        input_valid = self.check_input(self, root)

        # Case when input is valid
        if input_valid:

            # Retrieve the result
            dc_validations = self.bst_validation(self, root)
            dc_result = {
                "input_valid": input_valid,
                "bst_as_list": root,
                "bst_as_tree": Tree(nodes=root),
                "dc_validations": dc_validations,
                "bst_valid": dc_validations["result"]
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
root1 = [2,1,3]
root2 = [5,1,4,None,None,3,6]
root3 = []
root4 = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
root5 = [9,6,11,4,None,8,10,None,None,None,None,5]

# Executions
print("------------ Example 1 ------------")
dc_result_1 = Solution17.main(Solution17, root1)
print(dc_result_1)
print("------------ Example 2 ------------")
dc_result_2 = Solution17.main(Solution17, root2)
print(dc_result_2)
print("------------ Example 3 ------------")
dc_result_3 = Solution17.main(Solution17, root3)
print(dc_result_3)
print("------------ Example 4 ------------")
dc_result_4 = Solution17.main(Solution17, root4)
print(dc_result_4)
print("------------ Example 5 ------------")
dc_result_5 = Solution17.main(Solution17, root5)
print(dc_result_5)