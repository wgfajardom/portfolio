### Challenge 13
### Longest Substring Without Repeating Characters
### External Solution


### Definition of the solution

# Class for the solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length
    


### Testing External Solution

# Initialize inputs
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "abcdcefg"
s5 = "abcacbdd"

# Executions
print("------------ Example 1 ------------")
length_1 = Solution.lengthOfLongestSubstring(Solution, s1)
print(s1)
print(length_1)
print("------------ Example 2 ------------")
length_2 = Solution.lengthOfLongestSubstring(Solution, s2)
print(s2)
print(length_2)
print("------------ Example 3 ------------")
length_3 = Solution.lengthOfLongestSubstring(Solution, s3)
print(s3)
print(length_3)
print("------------ Example 4 ------------")
length_4 = Solution.lengthOfLongestSubstring(Solution, s4)
print(s4)
print(length_4)
print("------------ Example 5 ------------")
length_5 = Solution.lengthOfLongestSubstring(Solution, s5)
print(s5)
print(length_5)