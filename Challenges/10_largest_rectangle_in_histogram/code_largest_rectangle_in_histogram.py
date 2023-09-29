### Challenge 10
### Largest Rectangle in Histogram


### Definition of functions

# Check constraints
def initial_check(heights):
    
    # Variable for validation
    cl, ch = False, False

    # Check input lenght
    lh = len(heights)
    if 1 <= lh <= 105:
        cl = True

    # Check maximum allowed height
    if lh > 0:
        if (min(heights) >= 0) and (max(heights) <= 104):
            ch = True

    return all([ch, cl])


# Dimensions of the largest rectangle around a bin in the histogram
def dims_rectangle_by_bin(heights, bin_ref):

        # Number of bins in the histogram
        lh = len(heights)

        # Identifying bins having a height larger or equal than the reference height ('bin_height')
        ii = bin_ref
        bin_height = heights[ii] 
        fil_h = [h>=bin_height for h in heights]
        
        # Find width using the edges of the rectangle ('ind_sta' and 'ind_end')
        # Case when the reference bin is at the left edge of the histogram
        if ii == 0:
            ind_sta = 0
            if False in fil_h[ii:]: 
                ind_end = fil_h.index(False)
            else:
                ind_end = lh
        
        # Case when the reference bin is at the right edge of the histogram
        elif ii == lh-1:
            if False in fil_h[:ii]:
                r_fil_h = fil_h[::-1]
                ind_sta = lh-r_fil_h.index(False)
            else:
                ind_sta = 0
            ind_end = lh
        
        # The other cases
        else:
            if False in fil_h[:ii]:
                fil_h_aux = fil_h[:ii]
                r_fil_aux = fil_h_aux[::-1]
                ind_sta = len(fil_h_aux)-r_fil_aux.index(False)
            else:
                ind_sta = 0
            if False in fil_h[ii:]:
                fil_h_aux = fil_h[ii:]
                ind_end = ii+fil_h_aux.index(False)
            else:
                ind_end = lh

        # Computing rectangle dimensions (width and height), assuming a constant bin width
        bin_width = 1
        rectangle_width = bin_width*(ind_end-ind_sta)
        rectangle_height = bin_height

        return rectangle_width, rectangle_height, ind_sta, ind_end


# Find the largest rectangle in the histogram (main function)
def main(heights):

    # Verify initial validation by calling function 'initial_check'
    valid_input = initial_check(heights)
    
    # Case when input IS valid
    if valid_input == True:

        # Initialize variable where the result will be stored
        dc_results = {'area': 0}

        # Largest rectangle around each bin of the histogram
        for ii in range(len(heights)):
            
            # Call function 'dims_rectangle_by_bin'
            width, height, ind_sta, ind_end = dims_rectangle_by_bin(heights, ii)
                
            # Area calculation
            rectangle_area_aux = width*height
            if rectangle_area_aux > dc_results['area']:
                dc_results = {
                    'area': rectangle_area_aux, 
                    'w': width,
                    'h': height,
                    'index_left': ind_sta,
                    'index_right': ind_end,
                    'valid_input': True
                    }
                
        return dc_results
    
    # Case when input IS NOT valid
    else:
        dc_results = {'valid_input': False}
        return dc_results



### Execution of the main function

# Initialize inputs
heights_1 = [2,1,5,6,2,3]
heights_2 = [2,4]
heights_3 = [-1,7,3]
heights_4 = []
heights_5 = [3,1,5,9,6,7,9,2,5,2,3,4,3,6,7,1,8,6]

# Call the main fucntion
if __name__=='__main__':

    # Executions
    dc_1 = main(heights_1)
    dc_2 = main(heights_2)
    dc_3 = main(heights_3)
    dc_4 = main(heights_4)
    dc_5 = main(heights_5)

    # Retrieve results
    print('------- Example 1 -------')
    print(heights_1)
    print(dc_1)
    print('------- Example 2 -------')
    print(heights_2)
    print(dc_2)
    print('------- Example 3 -------')
    print(heights_3)
    print(dc_3)
    print('------- Example 4 -------')
    print(heights_4)
    print(dc_4)
    print('------- Example 5 -------')
    print(heights_5)
    print(dc_5)
