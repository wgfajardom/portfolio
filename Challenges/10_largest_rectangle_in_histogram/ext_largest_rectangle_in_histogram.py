### Challenge 10
### Largest Rectangle in Histogram
### External Solution


### Definition of the solution

# Class for the solution
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)

        left, stack = [0] * n, []
        for i in range(n):
            h, start = heights[i], i
            while stack and h <= heights[stack[-1]]:
                start = stack.pop()

            left[i] = (i - start) + left[start]
            stack.append(i)

        right, stack = [0] * n, []
        for i in reversed(range(n)):
            h, end = heights[i], i
            while stack and h <= heights[stack[-1]]:
                end = stack.pop()
            
            right[i] = (end - i) + right[end]
            stack.append(i)

        area = 0
        for i, height in enumerate(heights):
            width = right[i] + left[i] + 1
            area = max(area, width * height)
        return area



### Testing External Solution

# Initialize inputs
heights_1 = [2,1,5,6,2,3]
heights_2 = [2,4]
heights_3 = [-1,7,3]
heights_4 = []
heights_5 = [3,1,5,9,6,7,9,2,5,2,3,4,3,6,7,1,8,6]

# Executions
print('------- Example 1 -------')
result_1 = Solution.largestRectangleArea(Solution, heights_1)
print(heights_1)
print(result_1)
print('------- Example 2 -------')
result_2 = Solution.largestRectangleArea(Solution, heights_2)
print(heights_2)
print(result_2)
print('------- Example 3 -------')
result_3 = Solution.largestRectangleArea(Solution, heights_3)
print(heights_3)
print(result_3)
print('------- Example 4 -------')
result_4 = Solution.largestRectangleArea(Solution, heights_4)
print(heights_4)
print(result_4)
print('------- Example 5 -------')
result_5 = Solution.largestRectangleArea(Solution, heights_5)
print(heights_5)
print(result_5)
