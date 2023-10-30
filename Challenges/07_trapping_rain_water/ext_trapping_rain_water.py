### Challenge 07
### Trapping Rain Water
### External Solution



### Definition of the solution

# Time Complexity: O(N)
# Space Complexity: O(1)

# Class for the solution
class Solution:
    def trap(self, height: list[int]) -> int:
        i, j, ans, mx, mi = 0, len(height) - 1, 0, 0, 0
        # Two pointers 
        # Pointer i from the left
        # Pointer j from the right
        while i <= j:
            # Take the min height
            mi = min(height[i], height[j])
            # Find the max min height
            mx = max(mx, mi)
            # The units of water being tapped is the difference between max height and min height
            ans += mx - mi
            # Move the pointer i if height[i] is smaller
            if height[i] < height[j]: i += 1
            # Else move pointer j
            else: j -= 1
        return ans

    

### Testing External Solution

# Initialize inputs
h1 = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [4,2,0,3,2,5]
h3 = []
h4 = [1,2]
h5 = [4,2,2,3,1,0,4,1,5,2,1,2,3,0,1,0,1,0,2,0,2,0,3,1,4,3,2,1,5,2,1,2,3,1,0,1,0]

# Executions
print('------- Height profile 1 -------')
result_1 = Solution.trap(Solution,h1)
print(h1)
print(result_1)
print('------- Height profile 2 -------')
result_2 = Solution.trap(Solution,h2)
print(h2)
print(result_2)
print('------- Height profile 3 -------')
result_3 = Solution.trap(Solution,h3)
print(h3)
print(result_3)
print('------- Height profile 4 -------')
result_4 = Solution.trap(Solution,h4)
print(h4)
print(result_4)
print('------- Height profile 5 -------')
result_5 = Solution.trap(Solution,h5)
print(h5)
print(result_5) 
