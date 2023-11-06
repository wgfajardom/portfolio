### Challenge 09
### Number of Atoms
### External Solution



### Definition of the solution

# Import library
from collections import Counter

# Class for the solution
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, n = 0, len(formula)
        
        # Initialize a counter to keep track of the atoms
        count = Counter()
        stack = [count]

        # Loop through the formula
        while i < n:
            # '(' indicates the start of a new formula
            if formula[i] == '(':
                i += 1
                # Initialize a new counter for the new formula
                count = Counter()
                # Add the new counter to the stack
                stack.append(count)
            # ')' indicates the end of a formula
            elif formula[i] == ')':
                i += 1
                # Find the end of the count that follows the ')'
                end = i
                while i < n and formula[i].isdigit():
                    i += 1
                # Get the count, default to 1 if no count is provided
                mult = int(formula[end:i] or 1)
                top = stack.pop()
                # Add the count of each atom in the popped counter to the top counter in the stack
                for name, v in top.items():
                    stack[-1][name] += v * mult
                # Update the current counter to the top counter in the stack
                count = stack[-1]
            else:
                # If the current character is not '(' or ')', it's an atom
                # Find the end of the atom name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                # Get the atom name
                name = formula[start:i]
                # Find the end of the count that follows the atom name
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                # Get the count, default to 1 if no count is provided
                mult = int(formula[start:i] or 1)
                # Add the count of the atom to the top counter in the stack
                stack[-1][name] += mult

        # Return the count of all atoms in the format specified in the problem
        return "".join(name + (str(count[name]) if count[name] > 1 else '') for name in sorted(count))
    


### Testing External Solution

# Initialize inputs
formula_1 = "H2O"
formula_2 = "Mg(OH)2"
formula_3 = "K4(ON(SO3)2)2"
formula_4 = "(NH4)(NO3)"
formula_5 = "H2NCHRCOOH"

# Executions
print('------- Formula 1 -------')
o_formula_1 = Solution.countOfAtoms(Solution, formula_1)
print(formula_1)
print(o_formula_1)
print('------- Formula 2 -------')
o_formula_2 = Solution.countOfAtoms(Solution, formula_2)
print(formula_2)
print(o_formula_2)
print('------- Formula 3 -------')
o_formula_3 = Solution.countOfAtoms(Solution, formula_3)
print(formula_3)
print(o_formula_3)
print('------- Formula 4 -------')
o_formula_4 = Solution.countOfAtoms(Solution, formula_4)
print(formula_4)
print(o_formula_4)
print('------- Formula 5 -------')
o_formula_5 = Solution.countOfAtoms(Solution, formula_5)
print(formula_5)
print(o_formula_5)
