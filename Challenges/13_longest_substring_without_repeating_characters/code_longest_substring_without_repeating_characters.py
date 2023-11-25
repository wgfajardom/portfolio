### Challenge 13
### Longest Substring Without Repeating Characters



### Definition of the class solution

class Solution13:

    # Validate input
    def check_input(self, s:str) -> bool:

        # Initialize validations
        # sl: string length
        # vc: valid characters
        sl, vc = True, True

        # Perform validations
        if len(s) > 5e4:
            sl = False
        if s.isascii() == False:
            vc = False

        return all([sl,vc])


    # Check for repeated characters in a substring (ss)
    def repeated_characters(self, ss:str) -> bool:

        # Convert the string to a set
        set_ss = set(ss)

        # Compare the number of elements in the set to the string length
        rep_chars = len(set_ss) == len(ss)

        return rep_chars


    # Look for the longest substring without repeating characters using a sliding window
    def longest_ss_wrc(self, s:str) -> int | str:

        # Initialize parameters used in the while loop below
        sl = len(s)
        offset = 0
        aux_rc = False

        # Find the longest substring without repeating characters
        # Each step of the while loop uses a smaller sliding window
        # The for loop sweeps the input using a specific sliding window
        while aux_rc == False:

            sliding_window_size = sl-offset

            for ii in range(offset+1):
                # Auxiliar substring (aux_ss)
                # validation of ss as a non repeating characters substring (aux_rc)
                aux_ss = s[ii:ii+sliding_window_size]
                aux_rc = Solution13.repeated_characters(self, aux_ss)

                # Exit the for loop if a substring having non repeating characters is found
                if aux_rc == True:
                    break
            
            # Decrease the size of the sliding window
            if aux_rc == False:
                offset += 1

        # Result
        return sliding_window_size, aux_ss


    # Get the longest substring without repeating characters (main function)
    def main(self, s):

        # Validity input
        input_valid = Solution13.check_input(self, s)

        # Case input is vaid
        if input_valid:

            # Retrieve the result
            sliding_window_size, substring = Solution13.longest_ss_wrc(self, s)
            dc_result = {
                "input_valid": input_valid,
                "output": sliding_window_size,
                "substring": substring
            }

        # Case when input is not valid
        else:
            dc_result = {
                "input_valid": input_valid
            }

        return dc_result



### Execution of the main function

# Initialize inputs
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "abcdcefg"
s5 = "abcacbdd"

# Executions
print("------------ Example 1 ------------")
dc_result_1 = Solution13.main(Solution13, s1)
print(s1)
print(dc_result_1)
print("------------ Example 2 ------------")
dc_result_2 = Solution13.main(Solution13, s2)
print(s2)
print(dc_result_2)
print("------------ Example 3 ------------")
dc_result_3 = Solution13.main(Solution13, s3)
print(s3)
print(dc_result_3)
print("------------ Example 4 ------------")
dc_result_4 = Solution13.main(Solution13, s4)
print(s4)
print(dc_result_4)
print("------------ Example 5 ------------")
dc_result_5 = Solution13.main(Solution13, s5)
print(s5)
print(dc_result_5)
