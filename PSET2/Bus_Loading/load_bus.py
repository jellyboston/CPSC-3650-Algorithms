import sys

import bus


def main():
    try:
        cap = int(sys.stdin.readline())
    except ValueError:
        print("Non-integer input for bus capacity")
        return

    try:
        groups = [int(s) for s in sys.stdin.readline().split()]
    except ValueError:
        print("Non-integer input for sizes of groups")
        return

    try:
        validate_input(groups, cap)
    except ValueError as ex:
        print(ex)
        return

    solution = bus.optimize_loading(groups, cap)

    try:
        validate_solution(groups, cap, solution)
    except ValueError as ex:
        print(ex)
        return

    print(len(solution))

        
def validate_input(groups, cap):
    """ Throws a ValueError if the given input does not meet the preconditions of
        the problem.

        groups -- a list of integers
        l -- a number
    """
    # must have at least one group
    if len(groups) < 1:
        raise ValueError("Input must have at least 1 group")
    
    # groups must all have positive sizes
    if min(groups) <= 0:
        raise ValueError("Groups must have positive sizes")

    # capacity must be positive
    if cap <= 0:
        raise ValueError("Capacity of buses must be positive")
    
    # groups must not have size larger than capacity
    if max(groups) > cap:
        raise ValueError("Input has groups that won't fit on one bus")

    return


def validate_solution(groups, cap, solution):
    """ Throws an exception if the given solution is not a valid solution. """
    # check that solution starts with group 0
    if solution[0] != 0:
        raise ValueError("solution must start with group 0")

    # check that solution is increasing
    if len(solution) > 1 and min(solution[i] - solution[i - 1] for i in range(1, len(solution))) <= 0:
        raise ValueError("group indices in solution must be strictly increasing")

    # check that max group index is valid
    if solution[-1] >= len(groups):
        raise ValueError("group index out of range")
    
    # check that group chosen to travel together fit on buses
    for bus in range(len(solution) - 1):
        start = solution[bus]
        if bus != len(solution) - 1:
            # not last bus -- add up sizes of groups from first on this bus up
            # to but not including the first on the next bus
            count = sum(groups[start:solution[bus + 1]])
        else:
            # last bus -- add up sizes from first on this bus to end of groups
            count = sum(groups[start:])
        if count > cap:
            raise ValueError("overloaded bus")

    return


if __name__ == "__main__":
    main()
