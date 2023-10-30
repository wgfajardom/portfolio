### Challenge 06
### Shortest Palindrome
### External Solution


### Definition of the solution

# Class for the solution
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        # Reverse the original string and store it in a variable t
        t = s[::-1]

        # Iterate through each index i in the reversed string t
        for i in range(len(t)):
            
            # Check if the original string s starts with the suffix of t from index i to the end
            if s.startswith(t[i:]):
                
                # If a palindrome suffix is found, prepend the remaining characters in t to s to create the shortest palindrome
                return t[:i] + s

        # If a palindrome suffix is found, prepend the remaining characters in t to s to create the shortest palindrome
        return t + s



### Testing External Solution

# Initialize inputs
s1 = "aacecaaa"
s2 = "abcd"
s3 = "ina"

# Executions
result_1 = Solution.shortestPalindrome(Solution,s1)
result_2 = Solution.shortestPalindrome(Solution,s2)
result_3 = Solution.shortestPalindrome(Solution,s3)
print('------- Original string 1 -------')
print(s1)
print('------- Palindrome for string 1 -------')
print(result_1)
print('------- Original string 2 -------')
print(s2)
print('------- Palindrome for string 2 -------')
print(result_2)
print('------- Original string 3 -------')
print(s3)
print('------- Palindrome for string 3 -------')
print(result_3)
