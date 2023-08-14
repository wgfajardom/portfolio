### Challenge 08
### The latest time to catch a bus



### Definition of functions

# Check inputs
def verify_inputs(buses, passengers, capacity):
    
    # Initialize result variable
    valid_inputs = True
    message = "Inputs are valid."

    # Check inputs length
    n = len(buses)
    m = len(passengers)
    if (n == 0) or (n > 1e5) or (m == 0) or (m > 1e5) or (capacity == 0) or (capacity > 1e5):
        valid_inputs = False
        message = "Inputs are not valid. Length of buses, passengers, and capacity should be between 1 and 1e5."
    
    # Check inputs values
    buses_values = [b for b in buses if (b<2) or (b>1e9)]
    passengers_values = [p for p in passengers if (p<2) or (p>1e9)]
    if (len(buses_values) > 0) or (len(passengers_values) > 0):
        valid_inputs = False
        message = "Inputs are not valid. Values of buses and passengers should be between 2 and 1e9."

    # Check uniqueness of buses and passengers inputs
    lb_aux = len(list(set(buses)))
    lp_aux = len(list(set(passengers)))
    if (lb_aux != len(buses)) or (lp_aux != len(passengers)):
        valid_inputs = False
        message = "Inputs are not valid. There are repeated elements in buses or passengers inputs."

    return valid_inputs, message
    

# Assign passengers to buses based on their respective arrival times
def assign_passengers_to_buses(buses, passengers, capacity):

    # Sort inputs
    buses_s = sorted(buses)
    passengers_s = sorted(passengers)

    # Initialize list of lists passengers_by_bus
    passengers_by_bus = []

    # Fill passengers_by_bus
    # The ith sublist represents the passengers that catch the ith bus
    for ii in range(len(buses_s)):

        # Arrival time of the ith bus
        bus_time = buses_s[ii]
        
        # Passengers on queue when the ith bus arrives
        aux = [pass_time for pass_time in passengers_s if pass_time <= bus_time]

        # Passengers that catch the ith bus
        if len(aux) == 0:
            passengers_by_bus.append([])
        else:
            passengers_by_bus.append(aux[0:min(len(aux),capacity)])
            passengers_s = passengers_s[min(len(aux),capacity):]

    return sorted(passengers), passengers_by_bus


# Get the latest time to catch a bus (lttcab)
def latest_time(passengers_s, passengers_by_bus, capacity):

    # Arrival times of passengers that would catch the last bus
    times_last_bus = passengers_by_bus[-1]

    # Loop to determine lttcab
    number_iterations = 1
    lttcab = 0
    while lttcab == 0:

        # Case when there are still available slots in the last bus
        if len(times_last_bus) < capacity:
            lttcab = max(passengers_s)+1

        # Case when there are not available slots in the last bus
        elif len(times_last_bus) == capacity:

            # Difference between each consecutive pair of arrival times from passengers
            diffs = [[ii, times_last_bus[ii]-times_last_bus[ii-1]] for ii in range(1,len(times_last_bus))]
            
            # Possible spots between passengers
            possible_spots = [elem[0] for elem in diffs if elem[1] > 1]

            print(times_last_bus)
            print(diffs)
            print(possible_spots)
            # print(times_last_bus[max(possible_spots)])

            # Take the last available spot
            if len(possible_spots) > 0:
                lttcab = times_last_bus[max(possible_spots)]-1
            else:
                aux_lttcab = min(times_last_bus)-number_iterations
                # Be the first passenger of the last bus
                if aux_lttcab not in passengers_s:
                    lttcab = aux_lttcab
                # Repeat iterative loop
                else:
                    number_iterations += 1 

    return lttcab


# Last time to catch a bus based on buses capacity, buses and passengers arrival times (main function)
def main(buses, passengers, capacity):

    # Check validity of inputs by calling function 'verify_inputs'
    valid_inputs, message = verify_inputs(buses, passengers, capacity)

    # Scenarios depending on the validation of inputs
    if valid_inputs == True:
        
        # Determine passengers per bus by calling function 'assign_passengers_to_buses'
        passengers_s, passengers_by_bus = assign_passengers_to_buses(buses, passengers, capacity)

        # Obtain the latest time to catch a bus (lttcab) by calling function 'latest_time'
        lttcab = latest_time(passengers_s, passengers_by_bus, capacity)

        # Define result valid scenario
        dc_result = {"message":message, "passengers_by_bus":passengers_by_bus, "lttcab":lttcab}

    else:
        # Define result no valid scenario
        dc_result = {"message":message}

    return dc_result



### Execution of the main function

# Initialize inputs

buses_1 = [10,20]
passengers_1 = [2,17,18,19]
capacity_1 = 2

buses_2 = [20,30,10]
passengers_2 = [19,13,26,4,25,11,21]
capacity_2 = 2

buses_3 = [10,30,20,40,5]
passengers_3 = [6,7,8,9,12,19,24,25,26,27,28,29]
capacity_3 = 3

buses_4 = [10,20,20]
passengers_4 = [2,3,4,5]
capacity_4 = 3

buses_5 = [10,20,30]
passengers_5 = [1,2,3,4,5]
capacity_5 = 3



# Call the main function
if __name__ == '__main__':

    # Executions
    result_1 = main(buses_1, passengers_1, capacity_1)
    result_2 = main(buses_2, passengers_2, capacity_2)
    result_3 = main(buses_3, passengers_3, capacity_3)
    result_4 = main(buses_4, passengers_4, capacity_4)
    result_5 = main(buses_5, passengers_5, capacity_5)

    # Retrieve results
    print('------- Set of inputs 1 -------')
    print("Buses:", buses_1)
    print("Passengers:", passengers_1)
    print("Capacity:", capacity_1)
    print(result_1["message"])
    print("Passengers by bus:", result_1["passengers_by_bus"])
    print("Last time to catch a bus:", result_1["lttcab"])
    print('------- Set of inputs 2 -------')
    print("Buses:", buses_2)
    print("Passengers:", passengers_2)
    print("Capacity:", capacity_2)
    print(result_2["message"])
    print("Passengers by bus:", result_2["passengers_by_bus"])
    print("Last time to catch a bus:", result_2["lttcab"])
    print('------- Set of inputs 3 -------')
    print("Buses:", buses_3)
    print("Passengers:", passengers_3)
    print("Capacity:", capacity_3)
    print(result_3["message"])
    print("Passengers by bus:", result_3["passengers_by_bus"])
    print("Last time to catch a bus:", result_3["lttcab"])
    print('------- Set of inputs 4 -------')
    print("Buses:", buses_4)
    print("Passengers:", passengers_4)
    print("Capacity:", capacity_4)
    print(result_4["message"])
    print('------- Set of inputs 5 -------')
    print("Buses:", buses_5)
    print("Passengers:", passengers_5)
    print("Capacity:", capacity_5)
    print(result_5["message"])
