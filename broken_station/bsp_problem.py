# Helper function to count the removed stations based on the given distance using dynamic programming
def count_removed_dp(start, distance_left, length, L, memo):
    # Check if the result for the current parameters is already in the memo
    if (start, distance_left) in memo:
        return memo[(start, distance_left)]

    # Base case: if the start index is beyond the number of stations or if the distance left is zero
    if start >= length or distance_left == 0:
        return 0

    count = 0

    # Loop through the remove possible stations
    for i in range(start + 1, length):
        # Recursively count removed stations for the remaining stations and distance_left
        if L[i] - L[start] < distance_left:
            count += 1 + count_removed_dp(i, distance_left - (L[i] - L[start]), length, L, memo)

    # Memorize the count
    memo[(start, distance_left)] = count
    return count


# Function to return the maximum value possible of the closest two number in L, after removing m of the numbers
def bsp_value_dp(L, m):
    length = len(L)

    # Memorization dict to store computed results
    memo = {}
    low = 0
    high = L[-1] - L[0]

    # Binary search to find the maximum distance such that the number of removed stations doesn't exceed 'm
    while low < high:
        mid = (low + high + 1) // 2
        removed = count_removed_dp(0, mid, length, L, memo)

        # Adjust the parameters to remove the stations
        if removed > m:
            high = mid - 1
        else:
            low = mid

    return low


# Function to return the corresponding list after removing m value
def bsp_solution_dp(L, m):
    result = []

    # Calculate the max distance using the bsp_value_dp function
    max_distance = bsp_value_dp(L, m)

    length = len(L)
    last = L[0]
    result.append(last)
    temp = m

    # Construct the resultant list after station removal based on the maximum distance
    for i in range(1, length):
        if L[i] - last < max_distance and temp > 0:
            # Skip station if the distance to the last station is less than the max distance and removal limit is not
            # exhausted
            temp -= 1
        else:
            # Add station to the result list if the distance is greater or removal limit is reached
            result.append(L[i])
            last = L[i]

    return result  # Return the resultant list after removing stations


if __name__ == '__main__':
    L = [2, 4, 6, 7, 10, 14]
    m = 2
    value = bsp_value_dp(L, m)
    answer = bsp_solution_dp(L, m)
    print(answer)
    print(value)
