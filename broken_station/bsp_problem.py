def calculate_max(mem, L, m):
    max_value = 0

    # Base case: if list is empty return 0
    if len(L) == 0:
        return 0

    # Base case: if there are no more elements to be removed then,
    # return the minimum difference of the adjacent elements
    if m == 0:
        return min(L[i + 1] - L[i] for i in range(len(L) - 1))

    # Loop through each element of the list
    for i in range(len(L)):
        # Create a list with the current element removed
        mod_L = L[:i] + L[i + 1:]

        # Check if the value is located in memory or not
        # If it is not located then compute it and store the result
        if (tuple(mod_L), m - 1) not in mem:
            mem[tuple(mod_L), m - 1] = calculate_max(mem, mod_L, m - 1)

        # Retrieve the result from memory
        mem_value = mem[tuple(mod_L), m - 1]

        # Update the maximum value
        if mem_value > max_value:
            max_value = mem_value

    return max_value


def find_solution(mem, result):
    # Loop through the memory
    for key, val in mem.items():
        # Extract the list from the key
        curr_L = list(key[0])
        # Calculate the minimum difference of the adjacent elements
        min_diff = min(curr_L[i + 1] - curr_L[i] for i in range(len(curr_L) - 1))
        # If it is equal to the computed result then return the list as it meets the criteria
        if min_diff == result:
            return curr_L

    # Case if there is no list that meets the criteria of the result
    return []


def bsp_value(L, m):
    # Create the dict to store the results
    mem = {}
    return calculate_max(mem, L, m)


def bsp_solution(L, m):
    # Create the dict to store the results
    mem = {}

    # Calculate the maximum value to be used to get the solution
    result = calculate_max(mem, L, m)

    # Find the solution from the memory dict
    solution = find_solution(mem, result)

    return solution


if __name__ == '__main__':
    L = [2, 4, 6, 7, 10, 14]
    m = 4
    value = bsp_value(L, m)
    answer = bsp_solution(L,m)
    print(value)
    print(answer)
