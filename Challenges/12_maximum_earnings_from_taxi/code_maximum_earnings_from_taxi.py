### Challenge 12
### Maximum Earnings From Taxi



### Definition of functions

# Validate inputs
def check_inputs(n, rides):
    
    # Initialize boolean validators
    rol, ris, ril, rir, rit = True, True, True, True, True
    
    # Validate road length
    if (n < 1) and (n > 1e5):
        rol = False
        
    # Ride validations
    # 1. Each ride should be a list of three elements (start, end, tip) 
    # 2. Length range for each ride
    # 3. Start and end points should be located before the road end (n)
    # 4. Tip range for each ride

    for ride in rides:
        
        # Validation 1
        if len(ride) != 3:
            ris = False
            
        else:
            # Validation 2
            ride_length = ride[1] - ride[0]
            if (ride_length < 1) or (ride_length > 3e4):
                ril = False
            
            # Validation 3
            if (ride[0] > n) or (ride[1] > n):
                rir = False
            
            # Validation 4
            tip = ride[2]
            if (tip < 1) or (tip > 1e5):
                rit = False

    # Taking into account all the validations
    validations = [rol, ris, ril, rir, rit]
    overall_validation = all(validations)

    return overall_validation, validations 


# First-step: to initialize taxi path
def first_step(rides_sorted, dc_steps, ride_id):
    
    # Initialize path with a ride
    ride = rides_sorted[ride_id]
    ref_end = ride[1]
    path = [ride_id]
    
    # Available and restricted rides
    ar_rides = [True if r[0]>=ref_end else False for r in rides_sorted]
    
    # Verify if the path is finished
    fin_step = not(any(ar_rides))
    
    # Save path info
    key = "".join([str(p) for p in path])
    dc_steps[key] = {
        "path": path,
        "availability": ar_rides, 
        "final_step": fin_step,
        "parent": None
    }
    
    return dc_steps, key


# Forward-step: required when a path of the taxi has not been finished
# From current key to child key
def forward_step(rides_sorted, dc_steps, key, path, ar_rides):
    
    # Select next ride (suffix "c" means "child")
    id_n_ride = ar_rides.index(True)
    path_c = path + [id_n_ride]
    
    # New available and restricted rides
    ref_end_c = rides_sorted[id_n_ride][1]
    ar_rides_c = [True if r[0]>=ref_end_c else False for r in rides_sorted]

    # Verify is the new path is finished
    fin_step_c = not(any(ar_rides_c))

    # Save new path info
    key_c = "".join([str(p) for p in path_c])
    dc_steps[key_c] = {
        "path": path_c,
        "availability": ar_rides_c, 
        "final_step": fin_step_c,
        "parent": key
    }
    
    # Save key for the next step
    ns_key = key_c
    
    return dc_steps, ns_key


# Backward-step: required when a path of the taxi has not been finished
# From current key to parent key
def backward_step(dc_steps, key, path):

    # Retrieve information from the parent key (suffix "p" means "parent")
    key_p = dc_steps[key]["parent"]
    path_p = dc_steps[key_p]["path"]
    ar_rides_p = dc_steps[key_p]["availability"]
    fin_step_p = dc_steps[key_p]["final_step"]

    # Restrict the last ride of the child path in the parent path
    last_ride = path[-1]
    ar_rides_p[last_ride] = False
    
    # Verify is the new path is finished
    fin_step_p = not(any(ar_rides_p))

    # Save new path info
    dc_steps[key_p] = {
        "path": path_p,
        "availability": ar_rides_p, 
        "final_step": fin_step_p,
        "parent": dc_steps[key_p]["parent"]
    } 
    
    # Save key for the next step
    ns_key = key_p
    
    return dc_steps, ns_key
    

# Orchestration of the next step
def step(rides_sorted, dc_steps, key):
    
    # Retrive information from current key
    path = dc_steps[key]["path"]
    ar_rides = dc_steps[key]["availability"]
    fin_step = dc_steps[key]["final_step"]
    
    # Case for a forward-step (from current key to child key)
    if fin_step == False:
        dc_steps, ns_key = forward_step(rides_sorted, dc_steps, key, path, ar_rides)

    # Case for a backward-step (from current key to parent key)
    else:
        dc_steps, ns_key = backward_step(dc_steps, key, path)
    
    return dc_steps, ns_key


# Find all the possible sequences of rides (paths) for the taxi
def taxi_paths(rides_sorted, dc_steps):
    
    # Take into account all the possibilities for a first ride
    for first_ride_id in range(len(rides_sorted)): 
    
        # Assume the first ride
        dc_steps, key = first_step(rides_sorted, dc_steps, first_ride_id)
        ls_keys = dc_steps.keys()
        fin_paths = all([dc_steps[k]["final_step"] for k in ls_keys])
        
        # Find all possible taxi paths based on a selected first ride
        while fin_paths == False:
            
            # Give a step
            new_dc_steps, ns_key = step(rides_sorted, dc_steps, key)
            
            # Calculate whether all paths are finished
            fin_paths = all([dc_steps[k]["final_step"] for k in ls_keys])
            
            # Re-defined variable for next step
            dc_steps = new_dc_steps
            key = ns_key
    
    return dc_steps


# Compute the earnings generated by each taxi path
def earnings_by_path(rides_sorted, dc_steps):

    # Initiliaze variables where the taxi path with maximum earnings will be stored
    max_earnings, key_best_path = 0, ""
    
    # Computation of earnings by taxi path
    for k in dc_steps.keys():
        
        # Retrieve path
        p = dc_steps[k]["path"]
        
        # Earnings for the path
        earnings = 0
        for ride_id in p:
            tip = rides_sorted[ride_id][2]
            ride_length = rides_sorted[ride_id][1] - rides_sorted[ride_id][0]
            earnings += ride_length + tip
        
        # Update dictionary 'dc_steps' including earnings for the path
        dc_steps[k].update({"earnings": earnings})
    
        # Identify the taxi path with the maximum earnings
        if earnings > max_earnings:
            max_earnings, key_best_path = earnings, k

    return dc_steps, max_earnings, key_best_path    


# Find the taxi path having the maximum earnings (main function)
def main(n, rides):

    # Validate inputs
    overall_validation, validations = check_inputs(n, rides)
    
    # Case when inputs are valid
    if overall_validation == True:
    
        # Sort input rides
        rides_sorted = sorted(rides, key=lambda x: x[0])
    
        # Retrieve all possible taxi paths by calling the function 'taxi_paths'
        dc_steps = dict()
        dc_steps = taxi_paths(rides_sorted, dc_steps)
        
        # Calculate earnings from each taxi path by calling the function 'earnings_by_path'
        dc_steps, max_earnings, key_best_path = earnings_by_path(rides_sorted, dc_steps)
    
        # Retrieve all possible taxi paths and their earnings
        all_paths = [(dc_steps[k]["path"], dc_steps[k]["earnings"])  for k in dc_steps.keys()]
        
        # Best taxi path
        best_path_rides_ids = dc_steps[key_best_path]["path"]
        best_path_rides = [rides_sorted[ride_id] for ride_id in best_path_rides_ids]
        best_path = {
            'rides_ids': best_path_rides_ids, 
            'rides': best_path_rides,
            'max_earnings': max_earnings
        }
        
        # Overall results
        dc_overall = {
            'overall_validation': overall_validation,
            'rides_sorted': rides_sorted,
            'dc_steps': dc_steps,
            'all_paths': all_paths,
            'key_best_path': key_best_path,
            'best_path': best_path
        }
    
    # Case when inputs are not valid
    else:
        dc_overall = {
            'overall_validation': overall_validation,
            'validations': validations
        }

    return dc_overall



### Execution of the main function

# Initialize inputs
n1, rides_1 = 5, [[2,5,4],[1,5,1]]
n2, rides_2 = 20, [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
n3, rides_3 = 7, [[2,5,4],[1,5,1],[5,8,3]]

# Call the main fucntion
if __name__=='__main__':

    # Executions
    dc_overall_1 = main(n1, rides_1)
    dc_overall_2 = main(n2, rides_2)
    dc_overall_3 = main(n3, rides_3)

    # Retrieve results
    
    print('------- Example 1 -------')
    print('Inputs are valid:', dc_overall_1["overall_validation"])
    if dc_overall_1["overall_validation"] == True:
        print('All sorted rides')
        print(dc_overall_1["rides_sorted"])
        # print('Taxi paths and their respective earnings')
        # for ii in range(len(dc_overall_1["all_paths"])):
        #     print(dc_overall_1["all_paths"][ii])
        print('Best taxi path')
        print(dc_overall_1["best_path"])
        print('Maximum earnings:', dc_overall_1["best_path"]["max_earnings"])
    else:
        print('Detailed validations: road length, ride size, ride length, ride on road limits, tip limit')
        print(dc_overall_1["validations"])
        print(n1, rides_1)

    print('------- Example 2 -------')
    print('Inputs are valid:', dc_overall_2["overall_validation"])
    if dc_overall_2["overall_validation"] == True:
        print('All sorted rides')
        print(dc_overall_2["rides_sorted"])
        # print('Taxi paths and their respective earnings')
        # for ii in range(len(dc_overall_2["all_paths"])):
        #     print(dc_overall_2["all_paths"][ii])
        print('Best taxi path')
        print(dc_overall_2["best_path"])
        print('Maximum earnings:', dc_overall_2["best_path"]["max_earnings"])
    else:
        print('Detailed validations: road length, ride size, ride length, ride on road limits, tip limit')
        print(dc_overall_2["validations"])
        print(n2, rides_2)

    print('------- Example 3 -------')
    print('Inputs are valid:', dc_overall_3["overall_validation"])
    if dc_overall_3["overall_validation"] == True:
        print('All sorted rides')
        print(dc_overall_3["rides_sorted"])
        # print('Taxi paths and their respective earnings')
        # for ii in range(len(dc_overall_3["all_paths"])):
        #     print(dc_overall_3["all_paths"][ii])
        print('Best taxi path')
        print(dc_overall_3["best_path"])
        print('Maximum earnings:', dc_overall_3["best_path"]["max_earnings"])
    else:
        print('Detailed validations: road length, ride size, ride length, ride on road limits, tip limit')
        print(dc_overall_3["validations"])
        print(n3, rides_3)
