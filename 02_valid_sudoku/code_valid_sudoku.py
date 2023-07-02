### Challenge 02
### Valid Sudoku


### Import libraries
import numpy as np

### Definition of functions

# Load and check input
def load_board(input):

    # Convert to numeric list
    for ii in range(len(input)):
        for jj in range(len(input[ii])):
            # Replace "." by np.nan
            if input[ii][jj] == ".":
                input[ii][jj] = np.nan
            # Otherwise cast to integer
            else:
                input[ii][jj] = float(input[ii][jj])

    # Create matrix from numeric list
    main_array = np.array(input, dtype=float)

    # Check input size
    mas = main_array.shape
    nrows = mas[0]
    ncolumns = mas[1]
    if (nrows == 9) and (ncolumns == 9):
        check = True
    else:
        check = False

    # Result
    return main_array, check

# Building block for validations
def nine_elements_validation(array):
    aux_no_nan = np.sort(array[~np.isnan(array)])
    aux_unique = np.array(list(set(aux_no_nan)))
    if len(aux_no_nan) == len(aux_unique):
        validation = True
    else:
        validation = False
    return validation

# Validation over rows and columns
def valid_straight_lines(main_array, axis="rows"):
    ls_validation = [None]*9
    for ii in range(9):
        if axis == "columns":
            aux = main_array[ii][:]
        else: 
            aux = main_array[:][ii]
        ls_validation[ii] = nine_elements_validation(aux)
    return all(ls_validation)

# Validation over 3x3 sub-boxes
def valid_subboxes(main_array):
    ls_validation = [None]*9
    for ii in range(3):
        for jj in range(3):
            subbox = main_array[3*ii:3*(ii+1), 3*jj:3*(jj+1)]
            rs_subbbox = subbox.reshape(9)
            ls_validation[(3*ii)+jj] = nine_elements_validation(rs_subbbox)
    return all(ls_validation)


# Entire validation
def main(input):
    main_array, check = load_board(input)
    if check == True:
        vrows = valid_straight_lines(main_array,"rows")
        vcols = valid_straight_lines(main_array,"columns")
        vboxs = valid_subboxes(main_array)
        entire_validation = all([vrows,vcols,vboxs])
        return {"input_allowed": entire_validation,
                "valid_rows": vrows,
                "valid_columns": vcols,
                "valid_subboxes": vboxs}
    else:
        return {"input_allowed": False, 
                "message": "The input has to be a list of lists, representing a 9x9 sudoku block."}


### Execution of the entire validation (main function)

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
board_2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board_3 = [["5","4","3"]
,["2",".","."]
,[".","9","."]]

# Call the main function
if __name__ == '__main__':
    print('--------------------------------------------')   
    main_array_1, check_1 = load_board(board_1)
    print(main_array_1)
    print(main(board_1))
    print('--------------------------------------------')
    main_array_2, check_2 = load_board(board_2)
    print(main_array_2)
    print(main(board_2))
    print('--------------------------------------------')
    main_array_3, check_3 = load_board(board_3)
    print(main_array_3)
    print(main(board_3))
    print('--------------------------------------------')