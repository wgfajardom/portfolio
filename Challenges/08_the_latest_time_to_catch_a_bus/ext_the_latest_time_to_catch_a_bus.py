### Challenge 08
### The Latest Time to Catch a Bus
### External Solution


### Definition of the solution

# Class for the solution
class Solution:
    def latestTimeCatchTheBus(self, buses: list[int], passengers: list[int], capacity: int) -> int:
        
        # Sort inputs and get their sizes
        buses = sorted(buses)
        passengers = sorted(passengers)
        m, n = len(buses), len(passengers)

        # Initialize variable where the result will be stored
        latest_time = buses[len(buses) - 1]

        # Two-pointers
        i = j = 0
        cap = capacity
        while i < m and j < n:
            cur_bus = buses[i]
            cap = capacity
            while cap > 0 and j < n and passengers[j] <= cur_bus:
                j += 1
                cap -= 1
            i += 1

        # Reach final state
        if i == m:
            j -= 1
            # (1) buses * capacity > passengers
            if cap > 0 and passengers[j] != latest_time:
                return latest_time

            # (2) passengers > buses * capacity, find the largest possible time
            while j > 0:
                if passengers[j] - passengers[j - 1] > 1:
                    return passengers[j] - 1
                j -= 1
            return passengers[j] - 1
        else:
            return latest_time


        
### Testing External Solution

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


# Executions
print('------- Set of inputs 1 -------')
result_1 = Solution.latestTimeCatchTheBus(Solution, buses_1, passengers_1, capacity_1)
print(result_1)
print('------- Set of inputs 2 -------')
result_2 = Solution.latestTimeCatchTheBus(Solution, buses_2, passengers_2, capacity_2)
print(result_2)
print('------- Set of inputs 3 -------')
result_3 = Solution.latestTimeCatchTheBus(Solution, buses_3, passengers_3, capacity_3)
print(result_3)
print('------- Set of inputs 4 -------')
result_4 = Solution.latestTimeCatchTheBus(Solution, buses_4, passengers_4, capacity_4)
print(result_4)
print('------- Set of inputs 5 -------')
result_5 = Solution.latestTimeCatchTheBus(Solution, buses_5, passengers_5, capacity_5)
print(result_5)