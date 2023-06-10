import numpy as np
import code_valid_sudoku as vs   # Module from challenge 02

### Definition of functions

# First step function: sweep every cell to find its correct value
# It takes into account row, column, and subbox neighbors of each cell
def first_step(main_array):

    ref_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for ii in range(9):
        for jj in range(9):

            # Check if the value [ii][jj] is empty
            if np.isnan(main_array[ii,jj]):
            
                # Get row, column, and subbox related to the value [ii][jj]
                aux_row = main_array[ii,:]
                aux_col = main_array[:,jj]
                quo_ii, quo_jj = int(ii/3), int(jj/3)
                aux_sbx = main_array[3*quo_ii:3*(quo_ii+1), 3*quo_jj:3*(quo_jj+1)]
                
                # Flatten subbox array
                aux_sbx_flat = aux_sbx.reshape(9)
                
                # Concatenate three auxiliary arrays
                all_aux_arrays = np.concatenate((aux_row, aux_col, aux_sbx_flat), axis=None)
                
                # Array having numbers already occupied
                ar_no_nan = np.sort(all_aux_arrays[~np.isnan(all_aux_arrays)]).astype(int)
                
                # List of possible options for the value [ii][jj]
                possible_values = list(ref_set.difference(set(ar_no_nan)))
                
                # If there is only one possible value assign it to [ii][jj]
                if len(possible_values) == 1:
                    main_array[ii,jj] = possible_values[0]
    
    return main_array



# Auxiliary (I) function for second step function
def possible_values_in_subbox(main_array, row_block, col_block):

    # Redefine subbox parameters
    ii, jj = row_block, col_block    
    # Set of reference
    ref_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # Get subbox
    aux_sbx = main_array[3*ii:3*(ii+1), 3*jj:3*(jj+1)]
    # Flatten subbox array
    aux_sbx_flat = aux_sbx.reshape(9)
    # Array having numbers already occupied
    ar_no_nan = np.sort(aux_sbx_flat[~np.isnan(aux_sbx_flat)]).astype(int)
    # List of needed values inside the subbox
    possible_values = list(ref_set.difference(set(ar_no_nan)))
    
    return possible_values



# Auxiliary (II) function for second step function
def assign_value_into_empty_subbox_position(main_array, row_block, col_block, empty_indexes_sbx, value):

    # Redefine subbox parameters
    ii, jj = row_block, col_block

    # Search for the value row-wise within subboxes neighbors
    three_subboxes_rowwise = main_array[3*ii:3*(ii+1),:]
    aux_row_indices_to_block = np.argwhere(three_subboxes_rowwise==value)
    # print(len(aux_row_indices_to_block))
    if len(aux_row_indices_to_block) > 0:
        # Block rows from list of empty positions
        row_indices_to_block = [(3*ii)+index[0] for index in aux_row_indices_to_block]
        empty_indexes_sbx = [elem for elem in empty_indexes_sbx if elem[0] not in row_indices_to_block]

    # Search for the value column-wise within subboxes neighbors
    three_subboxes_colwise = main_array[:,3*jj:3*(jj+1)]
    aux_col_indices_to_block = np.argwhere(three_subboxes_colwise==value)
    # print(len(aux_col_indices_to_block))
    if len(aux_col_indices_to_block) > 0:
        # Block columns from list of empty positions
        col_indices_to_block = [(3*jj)+index[1] for index in aux_col_indices_to_block]
        empty_indexes_sbx = [elem for elem in empty_indexes_sbx if elem[1] not in col_indices_to_block]

    # Assign the value if only one position is allowed within the subbox
    # print(len(empty_indexes_sbx))
    if len(empty_indexes_sbx) == 1:
        main_array[empty_indexes_sbx[0][0], empty_indexes_sbx[0][1]] = value

    return main_array


# Second step function: finds the possible values within a subbox
# It takes into account subboxes that share the same rows or columns
def second_step(main_array):

    for ii in range(3):
        for jj in range(3):

            # print("|||||||||||||||||||||| ii={}, jj={} ||||||||||||||||||||||".format(ii, jj))
            
            # Call function 'possible_values_in_subbox'
            possible_values = possible_values_in_subbox(main_array, row_block=ii, col_block=jj)

            if len(possible_values) > 0:

                # Iterate over all possible values
                for value in possible_values:   
                    # print("****** value *******") 
                    # print(value)

                    # List of empty positions in the subbox
                    aux_empty_indexes = np.argwhere(np.isnan(main_array[3*ii:3*(ii+1), 3*jj:3*(jj+1)]))
                    empty_indexes_sbx = np.array([[(3*ii)+elem[0], (3*jj)+elem[1]] for elem in aux_empty_indexes])

                    # Call function 'assign_value_into_empty_subbox_position'
                    main_array = assign_value_into_empty_subbox_position(main_array, row_block=ii, col_block=jj, empty_indexes_sbx=empty_indexes_sbx, value=value)

    return main_array



# Solution of the Sudoku via iterations (main function)
def main(input):

    # Check the validity of the input
    valid_input = vs.main(input)

    # Case when the input is valid
    if valid_input["input_allowed"] == True:

        # Initialize variable for number of iterations
        number_iterations = 0

        # Empty cells are counted for the first time
        main_array = vs.load_board(input)[0]
        main_array_flat = main_array.reshape(81)
        number_empty_cells = len(list(main_array_flat[np.isnan(main_array_flat)]))

        # Iterations of the different step functions
        while number_empty_cells > 1:
            # print('----------------- main array ----------------- ')
            # print(main_array)
            main_array = first_step(main_array)
            # print('----------------- first step ----------------- ')
            # print(main_array)
            main_array = second_step(main_array)
            # print('----------------- second step ----------------- ')
            print(main_array)
            
            # Empty cells counted after each iteration
            main_array_flat = main_array.reshape(81)
            number_empty_cells = len(list(main_array_flat[np.isnan(main_array_flat)]))

            # Increase the number of iterations
            number_iterations += 1
            print(number_iterations)
            # if number_iterations == 2:
            #     break

        # Solution 
        result = {"original_board": vs.load_board(input)[0],
                  "valid_input": valid_input,
                  "solved": True,
                  "solution": main_array,
                  "number_iterations": number_iterations}
    
    # Case when the input is not valid
    else:
        result = {"original_board": vs.load_board(input)[0],
                  "valid_input": valid_input,
                  "solved": False}

    return result

### Execution of the Sudoku's solution (main function)

# Initialize inputs
board_1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board_2 = [[".",".",".",".",".",".",".",".","."]
,["7",".",".",".","8",".",".",".","5"]
,["2",".",".","9",".",".","3",".","."]
,["9",".",".","7",".",".",".",".","8"]
,["4","7",".","3",".",".",".","5","."]
,[".",".",".","4",".",".",".",".","1"]
,["5",".",".",".","6",".",".",".","2"]
,[".","1","4",".",".",".",".",".","."]
,[".",".","2",".","9",".",".","1","."]]



# Call the main function
if __name__ == '__main__':
    result = main(board_2)
    # print('---------------------- Original Board -----------------------')
    # print(result["original_board"])
    # print('----------------------- Is it valid? ------------------------')
    # print(result["valid_input"]["input_allowed"])
    # if result["solved"] == True:
    #     print('----------------------- Board Solved ------------------------')
    #     print(result["solution"])
    #     print('------------------- Number of iterations --------------------')
    #     print(result["number_iterations"])

