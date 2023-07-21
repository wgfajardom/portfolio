### Challenge 07
### Trapping Rain Water



### Import libraries
from matplotlib import pyplot as plt



### Definition of functions

# Input validation
def satisfy_constraints(height):
    
    # Initialize result
    valid_input = True
    
    # Check length
    if (len(height) == 0) or (len(height) >= 2e4):
        valid_input = False
    else:
        # Check minimum and maximum height
        if (min(height) < 0) or (max(height) > 105):
            valid_input = False

    return valid_input



# Look for and sort the local maxima of height
def local_maxima(height):

    # Input length
    lh = len(height)

    # Initialize list where local maxima indexes will be stored
    local_maxima_index = []

    # Filling the previous list
    for ii in range(lh):
        # Edge condition (left edge)
        if ii == 0:
            if height[ii] > height[ii+1]:
                local_maxima_index.append(ii)
        # Edge condition (right edge)           
        elif ii == lh-1:
            if height[ii] > height[ii-1]:
                local_maxima_index.append(ii)
        # Normal cases
        else:
            if (height[ii] > height[ii-1]) and (height[ii] > height[ii+1]):
                local_maxima_index.append(ii)

    # Ranking of local maxima heights from highest to lowest
    lm = [[id,height[id]] for id in local_maxima_index]
    sorted_lm = sorted(lm, key=lambda x: -x[1])    

    return sorted_lm



# Compute the water capacity
def water_capacity(height, sorted_lm):

    # Initialize capacity, prohibited indexes, index and value of global maximum
    total_capacity = 0
    cell_capacity = [0]*len(height)
    cell_capacity_to_plot = [0]*len(height)
    prohibited_indexes = []
    id_gm, he_gm = sorted_lm[0][0], sorted_lm[0][1]

    # Compute capacity of each the water well
    # Water well: portion of water between global maximum and a specific local maximum
    for kk in range(1,len(sorted_lm)):
        
        # Index and value of the local maximum
        id_lm = sorted_lm[kk][0]
        he_lm = sorted_lm[kk][1]

        # Height treshold for the water well
        ht = min(he_lm,he_gm)

        # Capacity of the water well
        # Iterations over the cells composing the water well
        for ii in range(min(id_lm,id_gm), max(id_lm,id_gm)+1):

            # Cell height must be less than height treshold, and cell index must not be prohibited
            if (height[ii] < ht) and (ii not in prohibited_indexes):
                
                # Capacity of each cell (column) from the water well
                cell_capacity[ii] = ht-height[ii]
                cell_capacity_to_plot[ii] = ht

                # Add cell capacity to the entire water capacity
                total_capacity += cell_capacity[ii]
                
                # Add the already considered index to the list of prohibited indexes
                prohibited_indexes.append(ii)

    return total_capacity, cell_capacity, cell_capacity_to_plot



# Generate plot of height and water profile
def plot_input(height, cell_capacity_to_plot, total_capacity):

    # Define variables to plot
    x_plot = [ii for ii in range(len(height)+1)] 
    y_plot = height + [height[-1]]
    water_plot = cell_capacity_to_plot + [cell_capacity_to_plot[-1]]

    # Plot height and water profile 
    # plt.plot(x_plot, y_plot, '-', color='firebrick', drawstyle='steps-post')
    plt.fill_between(x_plot, water_plot, step="post", color='aqua', alpha=0.75)
    plt.fill_between(x_plot, y_plot, step="post", color='firebrick', alpha=1.00)
    
    # Additional plot features
    y_max = max(height)
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off
    plt.axis('scaled')
    plt.xlim([-0.5, max(x_plot)+0.5])
    plt.ylim([-0.5, max(y_plot)+0.5])
    plt.yticks([ii for ii in range(y_max+1)])
    plt.title('Height profile {}. Water capacity: {}'.format("".join([str(c) for c in height]), total_capacity), fontsize=10)

    # Save and close figure
    plt.savefig("input_{}.png".format("".join([str(c) for c in height])))
    plt.close()



# Entire calculation of the trapped water within the height profile (main function)
def main(height):

    # Input validation by calling function 'satisfy constraints'
    valid_input = satisfy_constraints(height)

    # Normal scenario
    if valid_input and (len(height) > 2):

        # Retrieve local maxima sorted by height by calling function 'local_maxima'
        sorted_lm = local_maxima(height)

        # Retrieve water capacity by calling function 'water capacity'
        total_capacity, cell_capacity, cell_capacity_to_plot = water_capacity(height, sorted_lm)
        message = 'Valid input.'

        # Generate image of the height and water profiles by calling function 'plot_input'
        plot_input(height, cell_capacity_to_plot, total_capacity)

    # Dummy scenario
    elif (len(height)==1) or len(height)==2:
        total_capacity = 0
        cell_capacity = [0]*len(height)
        message = 'Dummy case, try using a longer input.'

    # Error scenario
    else:
        total_capacity = None
        cell_capacity = None
        message = 'Input is not valid. Input length (il) should be 1<=il<=2e4. Also, values must be within the range 0<=value<=105.'

    result = {"total_capacity": total_capacity, "cell_capacity": cell_capacity, "message": message}
    return result


    
### Execution of the main function

# Initialize inputs

h1 = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [4,2,0,3,2,5]
h3 = []
h4 = [1,2]
h5 = [4,2,2,3,1,0,4,1,5,2,1,2,3,0,1,0,1,0,2,0,2,0,3,1,4,3,2,1,5,2,1,2,3,1,0,1,0]

# Call the main function
if __name__ == '__main__':

    # Executions
    result_1 = main(h1)
    result_2 = main(h2)
    result_3 = main(h3)
    result_4 = main(h4)
    result_5 = main(h5)

    # Retrieve results
    print('------- Height profile 1 -------')
    print(h1)
    print(result_1["cell_capacity"])
    print(result_1["total_capacity"])
    print(result_1["message"])
    print('------- Height profile 2 -------')
    print(h2)
    print(result_2["cell_capacity"])
    print(result_2["total_capacity"])
    print(result_2["message"])
    print('------- Height profile 3 -------')
    print(h3)
    print(result_3["cell_capacity"])
    print(result_3["total_capacity"])
    print(result_3["message"])
    print('------- Height profile 4 -------')
    print(h4)
    print(result_4["cell_capacity"])
    print(result_4["total_capacity"])
    print(result_4["message"])
    print('------- Height profile 5 -------')
    print(h5)
    print(result_5["cell_capacity"])
    print(result_5["total_capacity"])
    print(result_5["message"])        
