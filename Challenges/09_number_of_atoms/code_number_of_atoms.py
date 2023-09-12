### Challenge 09
### Number of atoms



### Definition of functions


# Alpha encoding: discriminate between letters ("A") and other characters ("Z") in a formula
def a_encoder(formula):
    alpha_encode = ""
    for ii in range(len(formula)):
        char = formula[ii]
        if char.isalpha():
            alpha_encode = alpha_encode + "A"
        else:
            alpha_encode = alpha_encode + "Z"
    return alpha_encode


# Numerical encoding: discriminate between numbers ("Q") and other characters ("Z") in a formula
def n_encoder(formula):
    num_encode = ""
    for ii in range(len(formula)):
        char = formula[ii]
        if char.isdigit():
            num_encode = num_encode + "Q"
        else:
            num_encode = num_encode + "Z"
    return num_encode


# Parenthesis encoding: discriminate between parenthesis and numbers associated to them ("P"), other numbers ("N"), and other characters ("A") in a formula  
def p_encoder(formula, ind_numbers_parenthesis):
    par_encode = ""
    for ii in range(len(formula)):
        char = formula[ii]
        if (char == "(") or (char == ")") or (ii in ind_numbers_parenthesis):
            par_encode = par_encode + "P"
        elif (char.isdigit()) and (ii not in ind_numbers_parenthesis):
            par_encode = par_encode + "N"
        else:
            par_encode = par_encode + "A"
    return par_encode


## Find position of elements and parentheses
def find_element_indices(formula):
    
    # Lists to store the indices of elements and parentheses in the formula
    ind_elements = []
    l_parenthesis = []
    r_parenthesis = []
    
    # Find the indices of elements and parentheses
    for ii in range(len(formula)):
        char = formula[ii]
        if char.isupper():
            ind_elements.append(ii)
        if char == "(":
            l_parenthesis.append(ii)
        if char == ")":
            r_parenthesis.append(ii)
    
    # Reverse the order of left parentheses
    l_parenthesis = l_parenthesis[::-1]

    return ind_elements, l_parenthesis, r_parenthesis


## Find names of elements
def find_element_names(formula, ind_elements):
    
    # Names of each major element in the formula
    nam_elements = []
    
    # Call alpha encoding 
    alpha_encode = a_encoder(formula)
    
    # Find name of each element based on the index of uppercase letters and the alpha encoding
    for jj in range(len(ind_elements)):
        
        # Separate each element from the formula, including not desired characters ("Z")
        ind_sta = ind_elements[jj]
        if jj < len(ind_elements)-1:
            ind_end = ind_elements[jj+1]
        else:
            ind_end = len(formula)
        aux_alpha_encode = alpha_encode[ind_sta:ind_end]
        
        # Excluding not desired characters ("Z")
        if "Z" not in aux_alpha_encode:
            name = formula[ind_sta:ind_end]
        else:
            new_ind_end = ind_sta + aux_alpha_encode.index("Z")
            name = formula[ind_sta:new_ind_end]
            
        # Add element name to the list
        nam_elements.append(name)

    return nam_elements


## Identifying numbers associated to parenthesis
def number_of_parentheses(formula, r_parenthesis):
    
    # Number for each parenthesis (n_parenthesis) and indices of digits associated to parenthesis (ind_numbers_parenthesis)
    n_parenthesis = []
    ind_numbers_parenthesis = []
    
    # Call numerical encoding
    num_encode = n_encoder(formula)
    
    # Identifying numbers associated to parenthesis
    # Numbers associated to parentheses always are located after the right parentheses
    for kk in range(len(r_parenthesis)):
        
        # Looking for characters after each right parenthesis
        ind_r_par = r_parenthesis[kk]
        ind_sta = ind_r_par + 1
        # Case when the right parenthesis is at the end of the formula
        if ind_sta == len(formula):
            number = "1" 
        # Rest of the cases
        else:
            aux_num_encode = num_encode[ind_sta:] 
            
            # Find number for each parenthesis (number)
            # Indices of digits belonging to numbers associated to parenthesis (from ind_sta to ind_end)
            if "Z" not in aux_num_encode:
                ind_end = ind_sta + len(aux_num_encode)
                number = formula[ind_sta:ind_end]
            else:
                ind_end = ind_sta + aux_num_encode.index("Z")
                if ind_sta == ind_end:
                    number = "1"
                else:
                    number = formula[ind_sta:ind_end]
            for ll in range(ind_sta, ind_end):
                ind_numbers_parenthesis.append(ll)
        
        # Assign number to each parenthesis
        n_parenthesis.append(int(number))

    return n_parenthesis, ind_numbers_parenthesis


## First count of the number of atoms - without considering parenthesis
def first_count(formula, ind_elements, ind_numbers_parenthesis):

    # Number of atoms by each element in the formula
    nmb_elements = []
    
    # Call parenthesis encoding
    par_encode = p_encoder(formula, ind_numbers_parenthesis)
    
    # Identifying number of atoms per element
    for jj in range(len(ind_elements)):
        
        # Separate each element from the formula, including letters ("A"), numbers ("N"), and parentheses or number associated to them ("P")
        ind_sta = ind_elements[jj]
        if jj < len(ind_elements)-1:
            ind_end = ind_elements[jj+1]
        else:
            ind_end = len(formula)
        aux_par_encode = par_encode[ind_sta:ind_end]
        
        # Extract number from each substring
        if "N" not in aux_par_encode:
            number = "1"
        elif "P" not in aux_par_encode:
            number = formula[ind_sta+1:ind_end]
        else:
            new_ind_end = ind_sta + aux_par_encode.index("P")
            number = formula[ind_sta+1:new_ind_end]
        
        # Store number in the corresponding list
        nmb_elements.append(int(number))

    return nmb_elements


## Second count of the number of atoms - considering parenthesis
def second_count(l_parenthesis, r_parenthesis, n_parenthesis, ind_elements, nmb_elements):

    # Taking into account the effect of parentheses and its associated numbers
    for kk in range(len(r_parenthesis)):
        l_par = l_parenthesis[kk]
        r_par = r_parenthesis[kk]
        multiple = n_parenthesis[kk]
        
        # The number of atoms from elements within a parenthesis are multiplied by the corresponding number of the parenthesis
        for ii in range(len(ind_elements)):
            ind_elem = ind_elements[ii]
            if (ind_elem > l_par) and (ind_elem < r_par):
                nmb_elements[ii] = multiple*nmb_elements[ii]

    return nmb_elements


## Third count of the number of atoms - group by element
def third_count(ind_elements, nam_elements, nmb_elements):
    
    # Create result dictionary
    dc_number_atoms = dict()
    
    # Total number of atoms per element
    for ii in range(len(ind_elements)):
        key = nam_elements[ii]
        if key not in dc_number_atoms.keys():
            dc_number_atoms[key] = nmb_elements[ii]
        else:
            dc_number_atoms[key] = dc_number_atoms[key] + nmb_elements[ii]
            
    # String-like output
    output_formula = ""
    ls_keys = sorted(list(dc_number_atoms.keys()))
    for key in ls_keys:
        value = dc_number_atoms[key]
        if value != 1:
            output_formula = output_formula + key + str(value)
        else:
            output_formula = output_formula + key

    return dc_number_atoms, output_formula


# Find number of atoms per element (main function)
def main(formula):

    ## Call function 'find_element_indices'
    ind_elements, l_parenthesis, r_parenthesis = find_element_indices(formula)
    
    ## Call function 'find_element_names'
    nam_elements = find_element_names(formula, ind_elements)

    ## Call function 'number_of_parentheses'
    n_parenthesis, ind_numbers_parenthesis = number_of_parentheses(formula, r_parenthesis)
    
    ## Call function 'first_count'
    nmb_elements = first_count(formula, ind_elements, ind_numbers_parenthesis)
    
    ## Call function 'second_count'
    nmb_elements = second_count(l_parenthesis, r_parenthesis, n_parenthesis, ind_elements, nmb_elements)
    
    ## Call function 'third_count'
    dc_number_atoms, output_formula = third_count(ind_elements, nam_elements, nmb_elements)

    return dc_number_atoms, output_formula



### Execution of the main function

# Initialize inputs
formula_1 = "H2O"
formula_2 = "Mg(OH)2"
formula_3 = "K4(ON(SO3)2)2"
formula_4 = "(NH4)(NO3)"
formula_5 = "H2NCHRCOOH"


# Call the main function
if __name__ == '__main__':

    # Executions
    dc_1, o_formula_1 = main(formula_1)
    dc_2, o_formula_2 = main(formula_2)
    dc_3, o_formula_3 = main(formula_3)
    dc_4, o_formula_4 = main(formula_4)
    dc_5, o_formula_5 = main(formula_5)

    # Retrieve results
    print('------- Formula 1 -------')
    print(formula_1)
    print(o_formula_1)
    print(dc_1)
    print('------- Formula 2 -------')
    print(formula_2)
    print(o_formula_2)
    print(dc_2)
    print('------- Formula 3 -------')
    print(formula_3)
    print(o_formula_3)
    print(dc_3)
    print('------- Formula 4 -------')
    print(formula_4)
    print(o_formula_4)
    print(dc_4)
    print('------- Formula 5 -------')
    print(formula_5)
    print(o_formula_5)
    print(dc_5)
    
