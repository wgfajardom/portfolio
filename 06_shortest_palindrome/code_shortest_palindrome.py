### Challenge 06
### Shortest palindrome


# Check input size
def check_size(s_raw):
    max_allowed_size = 50000
    if len(s_raw) <= max_allowed_size:
        valid_input = True
    else:
        valid_input = False
    s = s_raw.lower()
    return valid_input, s


# Validate whether input is already a palindrome
def valid_palindrome(s):
    
    # Input size and initialize 'valid_pal' variable
    ls = len(s)
    valid_pal = True
    # Check if input is palindrome
    for ii in range(int(ls/2)):
        if s[ii] != s[ls-1-ii]:
            valid_pal = False
    
    return valid_pal


# Generate palindrome from input
def gen_palindrome(s):

    # Initialize index counter, auxiliar string, and 'valid_pal' variable
    ii = 0
    s_aux = s
    valid_pal = valid_palindrome(s)

    # Add character at the beginning of the string and check if the modified string is a palindrome
    # Iterative process
    while valid_pal == False:
        # Add character from original string
        new_char = s[ii+1]
        # Modified string, verifying if it is palindrome
        mod_s = new_char + s_aux
        valid_pal = valid_palindrome(mod_s)
        # Assignments to generate new iterations
        s_aux = mod_s
        ii += 1

    return(mod_s)


# Entire process (main function)
def main(s_raw):

    # Check if input is valid by calling function 'check_size'
    valid_input, s = check_size(s_raw)

    if valid_input == True:
        # Generate shortest palindrome by calling function 'gen_palindrome'
        mod_s = gen_palindrome(s)
    else:
        # Retrieve error message
        mod_s = "Input is not valid. Its size is longer than 50000 characters."
    
    return mod_s



### Generation of the shortest palindrome (main function)

# Initialize inputs
s1 = "aacecaaa"
s2 = "abcd"
s3 = "ina"


# Call the main function
if __name__ == '__main__':

    # Execution
    result_1 = main(s1)
    result_2 = main(s2)
    result_3 = main(s3)

    # Retrieve results
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
