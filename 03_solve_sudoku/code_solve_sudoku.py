import numpy as np
import code_valid_sudoku as vs   # Module from challenge 02

### Definition of functions

# Step function that finds the value for each cell
# It takes into account row, column, and subbox neighbors
def find_value(main_array):

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

        # Iterations of the function 'find_value'
        while number_empty_cells > 1:
            main_array = find_value(main_array)
            print(main_array)
            
            # Empty cells counted after each iteration
            main_array_flat = main_array.reshape(81)
            number_empty_cells = len(list(main_array_flat[np.isnan(main_array_flat)]))

            # Increase the number of iterations
            number_iterations += 1
            print(number_iterations)
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

# Call the main function
if __name__ == '__main__':
    result = main(board_2)
    print('---------------------- Original Board -----------------------')
    print(result["original_board"])
    print('----------------------- Is it valid? ------------------------')
    print(result["valid_input"]["input_allowed"])
    if result["solved"] == True:
        print('----------------------- Board Solved ------------------------')
        print(result["solution"])
        print('------------------- Number of iterations --------------------')
        print(result["number_iterations"])