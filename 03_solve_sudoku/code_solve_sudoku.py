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
# Get missing values from a subbox
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
# Assign value taking into account its presence in neighbor subboxes
def assign_value_into_empty_subbox_position(main_array, row_block, col_block, empty_indexes_sbx, value):

    # Redefine subbox parameters
    ii, jj = row_block, col_block

    # Search for the value row-wise within subboxes neighbors
    three_subboxes_rowwise = main_array[3*ii:3*(ii+1),:]
    aux_row_indices_to_block = np.argwhere(three_subboxes_rowwise==value)
    if len(aux_row_indices_to_block) > 0:
        # Block rows from list of empty positions
        row_indices_to_block = [(3*ii)+index[0] for index in aux_row_indices_to_block]
        empty_indexes_sbx = [elem for elem in empty_indexes_sbx if elem[0] not in row_indices_to_block]

    # Search for the value column-wise within subboxes neighbors
    three_subboxes_colwise = main_array[:,3*jj:3*(jj+1)]
    aux_col_indices_to_block = np.argwhere(three_subboxes_colwise==value)
    if len(aux_col_indices_to_block) > 0:
        # Block columns from list of empty positions
        col_indices_to_block = [(3*jj)+index[1] for index in aux_col_indices_to_block]
        empty_indexes_sbx = [elem for elem in empty_indexes_sbx if elem[1] not in col_indices_to_block]

    # Assign the value if only one position is allowed within the subbox
    if len(empty_indexes_sbx) == 1:
        main_array[empty_indexes_sbx[0][0], empty_indexes_sbx[0][1]] = value

    return main_array


# Second step function: find possible values within a subbox
# It takes into account already filled values from neighbor subboxes 
def second_step(main_array):

    for ii in range(3):
        for jj in range(3):
            
            # Call function 'possible_values_in_subbox'
            possible_values = possible_values_in_subbox(main_array, row_block=ii, col_block=jj)

            # Check if there are missing values in the subbox
            if len(possible_values) > 0:

                # Iterate over all possible values
                for value in possible_values:   

                    # List of empty positions in the subbox
                    aux_empty_indexes = np.argwhere(np.isnan(main_array[3*ii:3*(ii+1), 3*jj:3*(jj+1)]))
                    empty_indexes_sbx = np.array([[(3*ii)+elem[0], (3*jj)+elem[1]] for elem in aux_empty_indexes])

                    # Call function 'assign_value_into_empty_subbox_position'
                    main_array = assign_value_into_empty_subbox_position(main_array, row_block=ii, col_block=jj, empty_indexes_sbx=empty_indexes_sbx, value=value)

    return main_array


# Auxiliary (I) function for third step function
# Get all the available positions in the board for a specific value
def available_indexes_for_value(main_array, value):

    # Empty positions
    aux_empty_indexes = np.argwhere(np.isnan(main_array))
    empty_indexes = np.array([[elem[0],elem[1]] for elem in aux_empty_indexes])
    # print('Initial - empty_indexes')
    # print(empty_indexes)

    # Prohibited positions for value (row-wise and column-wise)
    aux_positions_to_block = np.argwhere(main_array==value)
    # print("aux_positions_to_block rowwise or columnwise")
    # print(aux_positions_to_block)
    if len(aux_positions_to_block) > 0:
        for elem_block in aux_positions_to_block:
            # Delete prohibited positions from empty positions
            empty_indexes = [ei for ei in empty_indexes if (ei[0] != elem_block[0]) and (ei[1] != elem_block[1])]
        # print('After block rowwise and columnwise - empty_indexes')
        # print(empty_indexes)

    # Prohibited positions for value (subbox)
    for ii in range(3):
        for jj in range(3):
            possible_values = possible_values_in_subbox(main_array, row_block=ii, col_block=jj)
            
            # Prohibited positions for value in subboxes that already had the value
            if value not in possible_values:
                # Delete prohibited positions from empty positions
                empty_indexes = [ei for ei in empty_indexes if ((ei[0] >= (3*ii)) and (ei[0] < 3*(ii+1)) and (ei[1] >= (3*jj)) and (ei[1] < 3*(jj+1))) == False]
    # print('After block subbox - empty_indexes')
    # print(empty_indexes)

    # Prohibited positions for value (subbox neighbors)
    for ii in range(3):
        for jj in range(3):

            # print("-------- ii={}, jj={} -----------".format(ii,jj))

            # Prohibited positions for value due to prohibitions from neighbor subboxes
            empty_indexes_subbox = [[ei[0], ei[1]] for ei in empty_indexes if ((ei[0] >= (3*ii)) and (ei[0] < 3*(ii+1)) and (ei[1] >= (3*jj)) and (ei[1] < 3*(jj+1))) == True]
            rows_to_block = list(set([ei[0] for ei in empty_indexes_subbox]))
            unique_row = len(rows_to_block)==1
            if unique_row:
                # print("rows_to_block", rows_to_block)
                # Delete prohibited positions from empty positions
                empty_indexes = [ei for ei in empty_indexes if (ei[0] != rows_to_block[0]) or ((ei[1] >= 3*jj) and (ei[1] < 3*(jj+1)))]
            
            cols_to_block = list(set([ei[1] for ei in empty_indexes_subbox]))
            unique_col = len(cols_to_block)==1
            if unique_col:
                # print("cols_to_block", cols_to_block)
                # Delete prohibited positions from empty positions
                empty_indexes = [ei for ei in empty_indexes if (ei[1] != cols_to_block[0]) or ((ei[0] >= 3*ii) and (ei[0] < 3*(ii+1)))]
    
    # print('After block subboxes neighbors - empty_indexes')
    # print(empty_indexes)

    return empty_indexes



# Third step function: finds the possible values within a subbox 
# It is based on prohibitions from neighbor subboxes
def third_step(main_array):

    # Iterate over all possible values
    for value in range(1,10):

        # if value == 3:

        # Call function 'available_indexes_for_value'
        empty_indexes = available_indexes_for_value(main_array, value=value)

        # Assign value if the subbox has only one available position
        for ii in range(3):
            for jj in range(3):
                empty_indexes_subbox = [[ei[0], ei[1]] for ei in empty_indexes if ((ei[0] >= (3*ii)) and (ei[0] < 3*(ii+1)) and (ei[1] >= (3*jj)) and (ei[1] < 3*(jj+1))) == True]
                # print("------- ii={}, jj={}, value={} -------".format(ii,jj,value))
                # print(empty_indexes_subbox)
                # print(len(empty_indexes_subbox))
                if len(empty_indexes_subbox)==1:
                    main_array[empty_indexes_subbox[0][0], empty_indexes_subbox[0][1]] = value

        # Alternative assignation rows
        for ii in range(3):
            for row in range(3*ii,3*(ii+1)):
                empty_indexes_neighbors = [[ei[0], ei[1]] for ei in empty_indexes if ei[0] == row]
                if len(empty_indexes_neighbors)==1:
                    main_array[empty_indexes_neighbors[0][0], empty_indexes_neighbors[0][1]] = value
        
        # Alternative assignation columns
        for jj in range(3):
            for col in range(3*jj,3*(jj+1)):
                empty_indexes_neighbors = [[ei[0], ei[1]] for ei in empty_indexes if ei[1] == col]
                if len(empty_indexes_neighbors)==1:
                    main_array[empty_indexes_neighbors[0][0], empty_indexes_neighbors[0][1]] = value

    return main_array


# Auxiliary (I) function for fourth step function
# Assign value by completing rows
def find_value_in_row(main_array, index, value):

    # Set of reference
    ref_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # Redefine parameter
    ii = index
    # Get line
    aux_line = main_array[ii,:]
    # Array having numbers already occupied
    ar_no_nan = np.sort(aux_line[~np.isnan(aux_line)]).astype(int)
    # List of needed values inside the subbox
    possible_values = list(ref_set.difference(set(ar_no_nan)))

    if value in possible_values:
        # Get empty row indexes for column jj
        empty_indexes_line = np.argwhere(np.isnan(aux_line))
        # Find prohibited row indexes for column jj
        empty_indexes_line = [eil for eil in empty_indexes_line if value not in main_array[:,eil]]
        # Assign value if there is only one position available in the line
        if len(empty_indexes_line)==1:
            main_array[ii,empty_indexes_line[0]] = value

    return main_array



# Auxiliary (II) function for fourth step function
# Assign value by completing columns
def find_value_in_column(main_array, index, value):

    # Set of reference
    ref_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # Redefine parameter
    jj = index
    # Get line
    aux_line = main_array[:,jj]
    # Array having numbers already occupied
    ar_no_nan = np.sort(aux_line[~np.isnan(aux_line)]).astype(int)
    # List of needed values inside the subbox
    possible_values = list(ref_set.difference(set(ar_no_nan)))

    if value in possible_values:
        
        # Get empty row indexes for column jj
        empty_indexes_line = np.argwhere(np.isnan(aux_line))
        # Find prohibited row indexes for column jj
        empty_indexes_line = [eil for eil in empty_indexes_line if value not in main_array[eil,:]]
        # Assign value if there is only one position available in the line
        if len(empty_indexes_line)==1:
            main_array[empty_indexes_line[0],jj] = value

    return main_array


# Fourth step function: finds the possible values within a line
# It assigns values by completing lines
def fourth_step(main_array):

    # Iterate from 1 to 9
    for value in range(1,10):

        # Assign values to lines (i.e. rows or columns)
        for ii in range(9):
            # Call function 'find_value_in_row'
            main_array = find_value_in_row(main_array, index=ii, value=value)
        for jj in range(9):
            # Call function 'find_value_in_column'
            main_array = find_value_in_column(main_array, index=jj, value=value)

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
            print('----------------- first step ----------------- ')
            main_array = first_step(main_array)
            print(main_array)
            print('----------------- second step ----------------- ')
            main_array = second_step(main_array)
            print(main_array)
            print('----------------- third step ----------------- ')
            main_array = third_step(main_array)
            print(main_array)
            print('----------------- fourth step ----------------- ')
            main_array = fourth_step(main_array)
            print(main_array)

            # Empty cells counted after each iteration
            main_array_flat = main_array.reshape(81)
            number_empty_cells = len(list(main_array_flat[np.isnan(main_array_flat)]))

            # Increase the number of iterations
            number_iterations += 1
            print(number_iterations)
            if number_iterations == 4:
                break

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
board_3 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board_4 = [["2","5",".",".",".",".",".",".","4"]
,[".",".",".",".","5",".",".",".","9"]
,[".","8",".","3",".",".","2","5","."]
,[".",".",".",".",".",".",".",".","2"]
,[".","3",".",".",".","7",".",".","."]
,["8",".",".",".","4",".","1","6","."]
,["1",".",".",".","6",".","5","8","."]
,[".",".",".",".",".",".",".","9","."]
,[".",".","6","4",".",".",".",".","."]]


board_4_aux = [["2","5",".",".",".",".",".",".","4"]
,[".",".",".",".","5",".",".",".","9"]
,[".","8",".","3",".",".","2","5","7"]
,[".",".",".",".",".",".","3","7","2"]
,[".","3",".",".",".","7","9","4","8"]
,["8",".",".",".","4","3","1","6","5"]
,["1",".",".",".","6",".","5","8","3"]
,[".",".","8",".",".",".","4","9","6"]
,[".","9","6","4",".",".","7","2","1"]]





# Call the main function
# if __name__ == '__main__':
#     result = main(board_4)
#     # print('---------------------- Original Board -----------------------')
#     # print(result["original_board"])
#     # print('----------------------- Is it valid? ------------------------')
#     # print(result["valid_input"]["input_allowed"])
#     # if result["solved"] == True:
#     #     print('----------------------- Board Solved ------------------------')
#     #     print(result["solution"])
#     #     print('------------------- Number of iterations --------------------')
#     #     print(result["number_iterations"])


