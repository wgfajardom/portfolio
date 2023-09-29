### Challenge 11
### Median of two sorted arrays



### Definition of functions

# Validate constraints on inputs
def check_inputs(nums1, nums2):
    
    # Initialize variables for validation
    cm, cn, cv1, cv2 = False, False, True, True
    
    # Check the length of each input
    m = len(nums1)
    n = len(nums2)
    if 0 <= m <= 1000:
        cm = True
    if 0 <= n <= 1000:
        cn = True
    
    # Check the value of each element on the lists
    for e1 in nums1:
        if (e1 < 1e-6) or (e1 > 1e6):
            cv1 = False
    for e2 in nums2:
        if (e2 < 1e-6) or (e2 > 1e6):
            cv2 = False

    # Join all validations
    valid_inputs = all([cm, cn, cv1, cv2])
    return valid_inputs


# Compute median from a single sorted array
def median_sa(x):
    
    # Number of elements of the input
    n = len(x)
    
    # Case when n is even
    if len(x)%2 == 0:
        li = int(n/2)-1
        ri = int(n/2)
        median = (x[li]+x[ri])/2
    
    # Case when n is even
    else:
        ci = int(n/2)
        median = x[ci]
    
    return median


# Calculate median from two arrays (main function)
def main(nums1, nums2):

    # Call function 'check_inputs'
    valid_inputs = check_inputs(nums1, nums2)
    
    # Case when inputs are valid
    if valid_inputs == True:
    
        # Join and sort inputs
        x_raw = nums1 + nums2
        x = sorted(x_raw)
        
        # Call function 'median_sa'
        median = median_sa(x)
        dc_result = {
            'valid_inputs': valid_inputs,
            'median': median
        }
    
    # Case when inputs are not valid
    else:    
        dc_result = {
            'valid_inputs': valid_inputs,
            'error_message': "The inputs (nums1, nums2, or both) do not fulfill any of these conditions: a) 0 <= len(input) <= 1000, b) 1e-6 <= input[i] <= 1e6."
        }
    
    return dc_result



### Execution of the main function

# Initialize inputs
nums1 = [1,3]
nums2 = [2]
nums3 = [5e-7,0]
nums4 = [1,2]
nums5 = [3,4]
nums6 = [10,6,4]
nums7 = [4,6,4,1]


# Call the main function
if __name__ == '__main__':

    # Executions
    dc_1 = main(nums1, nums2)
    dc_2 = main(nums1, nums3)
    dc_3 = main(nums4, nums5)
    dc_4 = main(nums6, nums7)

    # Retrieve results
    print('------- Example 1 -------')
    print(nums1, nums2)
    print(dc_1)
    print('------- Example 2 -------')
    print(nums1, nums3)
    print(dc_2)
    print('------- Example 3 -------')
    print(nums4, nums5)
    print(dc_3)
    print('------- Example 4 -------')
    print(nums6, nums7)
    print(dc_4)
