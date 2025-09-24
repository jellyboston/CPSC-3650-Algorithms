'''
Constraints:
1. No bus may be loaded beyond its capacity
2. All buses have the same capacity
3. Groups loaded first-come-first-serve
4. No group may be split across multiple busses

Runtime: theta(n) algorithm

Inputs: (non-empty list [GroupSize], bus_capacity)
- NOTE: Bus capacity is positive and will be at least as large as the largest group

Return: list[index of the first group of each bus]
'''

def optimize_loading(groups, cap):
    """ Determines an optimal (fewest buses) way to load groups of the given
        sizes onto buses of the given capacity.  The solution is returned
        as a list of indices of the first group on each bus, so groups
        solution[0], ..., solution[1] - 1 go on the first bus, etc.

        groups -- a non-empty list of nonnegative integers
        cap -- an integer at least as large as each element in groups
    """
    # YOUR SOLUTION HERE
    # Greedy choice: select the smallest group size
    # Init counters and return
    bus_starts = []
    cap_sum, i = 0, 0
    while i < len(groups):
        if cap_sum + groups[i] <= cap:
            if cap_sum == 0:
                # Mark as starting group in bus
                bus_starts.append(i)
            cap_sum += groups[i]
            i += 1
        else:
            cap_sum = 0
    return bus_starts
