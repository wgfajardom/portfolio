### Challenge 15
### Reverse Nodes in k-Group



### Definition of the class solution

class Solution15:

    # Validate input
    def check_input(self, head:list, k:int) -> bool:

        # Initialize validations
        # hl: head length must be between 1 and 5000
        # kl: k should less or equal than head length
        # hv: head elements must be between 0 and 1000
        hl, kl, hv = True, True, True

        # Perform validations
        if (len(head) < 1) or (len(head) > 5000):
            hl = False
        if (k > len(head)) or (k < 1):
            kl = False
        for elem in head:
            if (elem < 0) or (elem >= 1000):
                hv = False

        return all([hl, kl, hv])


    # Reverse a k-group from the reference index (ref_ii)
    def single_reverse(self, head:list, k:int, ref_ii:int) -> list:

        # The reverse operation is carried out in an auxiliary variable
        aux_head = head.copy()

        # Assuring the k-group do not exceed heads length
        if ref_ii+k <= len(head):

            # Single reverse
            ii_offset = 1
            for ii in range(ref_ii, ref_ii+k, 1):
                aux_head[ii] = head[ref_ii+k-ii_offset]
                ii_offset += 1

        return aux_head
    

    # Multiple reverses of k-groups operating over a sliding window
    def multiple_reverses(self, head:list, k:int) -> list:

        # Initializing auxiliary variables
        ref_ii = 0
        remaining_head = len(head)

        # Carried out reverse operation iteratively
        while remaining_head/k >= 1:

            # Perform single reverse operation
            new_head = Solution15.single_reverse(self, head, k, ref_ii)

            # Recalculate auxiliary variables (moving sliding window)
            ref_ii += k
            remaining_head -= k
            head = new_head.copy()
            
        return head


    # Reverse nodes in k-groups (main function)
    def main(self, head:list, k:int):

        # Validation of inputs
        input_valid = Solution15.check_input(self, head, k)

        # Case when input is valid
        if input_valid:

            # Retrieve the result
            head_res = Solution15.multiple_reverses(self, head, k)
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
head2, k2 = [1,2,3,4,5], 3
head3, k3 = [1,2,3,4,5,6,7,8,9], 3
head4, k4 = [1,2,3,4,5,6,7], 9

# Executions
print("------------ Example 1 ------------")
dc_result_1 = Solution15.main(Solution15, head1, k1)
print(dc_result_1)
print("------------ Example 2 ------------")
dc_result_2 = Solution15.main(Solution15, head2, k2)
print(dc_result_2)
print("------------ Example 3 ------------")
dc_result_3 = Solution15.main(Solution15, head3, k3)
print(dc_result_3)
print("------------ Example 4 ------------")
dc_result_4 = Solution15.main(Solution15, head4, k4)
print(dc_result_4)