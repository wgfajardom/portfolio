### Challenge 04
### Repeated DNA Sequences
### External Solution



### Definition of the solution

# Class for the solution
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        
        # Initialize dictionary
        m = {}
        
        # Fill dictionary with sequences of ten characters
        for i in range(len(s)):
            m[s[i : i + 10]] = 1 + m.get(s[i : i + 10], 0)
        
        # Select the sequences that occur more than once in the DNA chain
        result = [key for key, value in m.items() if value > 1]
        
        return result



### Testing External Solution

# Initialize inputs
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAAAA"

# Executions
print("------- Repeated sequences -------")
print(Solution.findRepeatedDnaSequences(Solution, s))
