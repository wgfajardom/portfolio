### Challenge 14
### Minimum Number of K Consecutive Bit Flips



### Definition of the class solution

class Solution14:

    # Validate input
    def check_input(self, nums:list, k:int) -> bool:

        # Initialize validations
        # nl: nums length
        # kl: k should less or equal than nums length
        # bv: nums elements must be bits (0 or 1)
        nl, kl, bv = True, True, True

        # Perform validations
        if (len(nums) < 1) or (len(nums) > 1e5):
            nl = False
        if k > len(nums):
            kl = False
        for elem in nums:
            if (elem != 0) and (elem != 1):
                bv = False

        return all([nl, kl, bv])


    # Flip consecutive k bits from the reference index (ref_ii)
    def flip_con_bits(self, nums:list, k:int, ref_ii:int) -> list:

        # Bit flips are carried out in an auxiliary variable
        aux_nums = nums.copy()

        # Assuring the k-consecutive bits do not exceed nums length
        if ref_ii+k <= len(nums):

            # Individual bit flips
            for ii in range(ref_ii, ref_ii+k, 1):
                if aux_nums[ii] == 0:
                    aux_nums[ii] = 1
                else:
                    aux_nums[ii] = 0
        
        return aux_nums
    

    # Iterative flips to convert nums into a list full of '1's
    def flips(self, nums:list, k:int) -> int | list:

        # Initialize solution flag, repetition flag, list of nums states, and number of flips
        sol_flag = sum(nums) == len(nums)
        rep_flag = False
        ls_nums_states = [nums]
        nf = 0
        
        # Perform iterative flips
        while (sol_flag == False) and (rep_flag == False):

            # Single flip from reference index
            ref_index = nums.index(0)
            nums = Solution14.flip_con_bits(Solution14, nums, k, ref_index)
            nf += 1

            # Check if current nums state existed
            if nums in ls_nums_states:
                rep_flag = True
            else:
                ls_nums_states.append(nums)

            # Check if solution was achieved
            if sum(nums) == len(nums):
                sol_flag = True

        # Retrive result when conversion is not possible
        if rep_flag:
            return -1, ls_nums_states
        # Retireve result when conversion is possible, returning number of flips required 
        else:
            return nf, ls_nums_states


    # Find the minimum number of flips (main function)
    def main(self, nums:list, k:int):

        # Validation of inputs
        input_valid = Solution14.check_input(self, nums, k)

        # Case when input is valid
        if input_valid:

            # Retrieve the result
            nf, nums_history = Solution14.flips(self, nums, k)
            dc_result = {
                "input_valid": input_valid,
                "number_flips": nf,
                "nums_history": nums_history
            }

        # Case when input is not valid
        else:
            # Retrieve the result
            dc_result = {
                "input_valid": input_valid
            }

        return dc_result



### Execution of the main function

# Initialize inputs
nums1, k1 = [0,1,0], 1
nums2, k2 = [1,1,0], 2
nums3, k3 = [0,0,0,1,0,1,1,0], 3
nums4, k4 = [0,0,0,1,0,1,1,0], 10
nums5, k5 = [0,1,0,0,0], 2

# Executions
print("------------ Example 1 ------------")
dc_result_1 = Solution14.main(Solution14, nums1, k1)
print(dc_result_1)
print("------------ Example 2 ------------")
dc_result_2 = Solution14.main(Solution14, nums2, k2)
print(dc_result_2)
print("------------ Example 3 ------------")
dc_result_3 = Solution14.main(Solution14, nums3, k3)
print(dc_result_3)
print("------------ Example 4 ------------")
dc_result_4 = Solution14.main(Solution14, nums4, k4)
print(dc_result_4)
print("------------ Example 5 ------------")
dc_result_5 = Solution14.main(Solution14, nums5, k5)
print(dc_result_5)