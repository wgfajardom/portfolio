### Challenge 12
### Maximum Earnings From Taxi
### External Solution


### Definition of the solution

# Class for the solution
class Solution:

    # Improving performance with binary search
    def maxTaxiEarningsBinarySearch(self, n: int, rides: list[list[int]]) -> int:
        total_rides = len(rides)
        rides.sort(key=lambda x:x[1])
        table = [0]*(len(rides)+1)

        for i in range(1, len(rides) + 1):
            # Fill in table[i]
            currRide = rides[i-1]

            # If we don't choose the current ride
            maxEarningWithoutCurrentRide = table[i-1]

            # If we choose the current ride
            earningUpToPrevRide = 0
            low, high = 0, i-2
            while low <= high:
                mid = low + (high - low) // 2
                # Find the first ride that has end point before the start point of the current ride
                midRide = rides[mid]
                if midRide[1] <= currRide[0]:
                    low = mid + 1
                else:
                    high = mid - 1
            # high is pointing to the first ride that has end point before the start point of the current ride.
            earningUpToPrevRide = table[high+1]
            currentRideEarning = currRide[1] - currRide[0] + currRide[2]

            table[i] = max(maxEarningWithoutCurrentRide, currentRideEarning + earningUpToPrevRide)
        return table[-1]



### Testing External Solution

# Initialize inputs
n1, rides_1 = 5, [[2,5,4],[1,5,1]]
n2, rides_2 = 20, [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
n3, rides_3 = 7, [[2,5,4],[1,5,1],[5,8,3]]

# Executions
print('------- Example 1 -------')
result_1 = Solution.maxTaxiEarningsBinarySearch(Solution, n1, rides_1)
print(n1)
print(rides_1)
print(result_1)
print('------- Example 2 -------')
result_2 = Solution.maxTaxiEarningsBinarySearch(Solution, n2, rides_2)
print(n2)
print(rides_2)
print(result_2)
print('------- Example 3 -------')
result_3 = Solution.maxTaxiEarningsBinarySearch(Solution, n3, rides_3)
print(n3)
print(rides_3)
print(result_3)