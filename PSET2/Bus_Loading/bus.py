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
    # Greedy choice: sort to select the smallest group size
    groups.sort()

    # Init counters and return
    group_index = []
    cap_sum, group_ct = 0, 0
    for i in range(len(groups)):
        group_index.append(i)
        while cap_sum <= cap:
            cap_sum += groups[i]
            i += 1
        # Once full reset and move to the next bus
        cap_sum = 0
        group_ct += 1
    return group_index
