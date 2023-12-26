### Challenge 14
### Minimum Number of K Consecutive Bit Flips
### External Solution


### Definition of the solution

# Class for the solution
class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        # Total number of flips
        res = 0
        # Total times the iteration index has been flipped
        flippedCount = 0

        for i, num in enumerate(nums):
            # Decrement flipped count for the current index when previous flips
            # are outside of the window
            if i >= k and nums[i - k] > 1:
                nums[i - k] -= 2
                flippedCount -= 1
          
            # An even flipped count means that after all the previous flips, if 
            # any, the current number is now 0, which needs to be flipped
            if flippedCount % 2 == num:
                # K-bit flip is not possible if additional bits need to be flipped 
                # at the end of all valid window flips
                if i > len(nums) - k:
                    return -1

                # Flip the current number and increment flipped count
                nums[i] += 2
                flippedCount += 1
                res += 1

        return res
    


### Testing External Solution

# Initialize inputs
nums1, k1 = [0,1,0], 1
nums2, k2 = [1,1,0], 2
nums3, k3 = [0,0,0,1,0,1,1,0], 3
nums4, k4 = [0,0,0,1,0,1,1,0], 10
nums5, k5 = [0,1,0,0,0], 2

# Executions
print("------------ Example 1 ------------")
res_1 = Solution.minKBitFlips(Solution, nums1, k1)
print(res_1)
print("------------ Example 2 ------------")
res_2 = Solution.minKBitFlips(Solution, nums2, k2)
print(res_2)
print("------------ Example 3 ------------")
res_3 = Solution.minKBitFlips(Solution, nums3, k3)
print(res_3)
print("------------ Example 4 ------------")
res_4 = Solution.minKBitFlips(Solution, nums4, k4)
print(res_4)
print("------------ Example 5 ------------")
res_5 = Solution.minKBitFlips(Solution, nums5, k5)
print(res_5)