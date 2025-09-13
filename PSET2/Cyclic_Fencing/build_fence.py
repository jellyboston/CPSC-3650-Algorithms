import sys

import fence


def main():
    try:
        l = float(sys.stdin.readline())
    except ValueError:
        print("Non-numeric input for L")
        return

    try:
        d = [float(s) for s in sys.stdin.readline().split()]
    except ValueError:
        print("Non-numeric input for locations of trees")
        return

    try:
        validate_input(d, l)
    except ValueError as ex:
        print(ex)
        return

    solution = fence.optimize_fence(d, l)
    #print(solution)
    #solution = [float(s) for s in sys.stdin.readline().split()]

    try:
        validate_solution(d, l, solution)
    except ValueError as ex:
        print(ex)
        return

    expected_length = len(brute_force_optimize(d, l))
    if len(solution) < expected_length:
        print("Better than possible?  We only get here if Prof. Glenn made a mistake.")
    elif len(solution) > expected_length:
        print("Expected length", expected_length, "got", solution)
    else:
        print("PASSED")


def brute_force_optimize(d, l):
    """ Finds the minimum fence by finding all greedy solitions from all possible starting points """
    # This is not a proper solution because it does not meet the time bound!

    best = None
    
    # try all starting points
    start = 0
    while d[start] < l:
        # move points before start to end
        translated = d[start:]
        for i in range(1, start + 1):
            translated.append(d[i] + d[-1])
            
        # build the greedy fence starting at l
        candidate = greedy_fence(translated, l)
        if best is None or len(candidate) < len(best):
            best = candidate
        start = start + 1
    return best


def greedy_fence(d, l):
    """ Returns a subsequence of d that starts at 0.0 and ends at d[len(d)-1] such that
        consecutive elements of d are no more then L apart and the length of the returned
        list is as short as possible given that condition.

        d -- an increasing list of at least two numbers giving the locations of
             the corners of the house and the trees where fence segments can end
        l -- a positive number no less that the greatest difference between consecutive elements of d
    """
    ends = [d[0]] # where the endpoints of the fence segments are; first is at corner of house
    for i in range(1, len(d)):
        if d[i] - ends[-1] > l:
            # can't get from last endpoint to d[i]
            ends.append(d[i - 1])
    ends.append(d[-1]) # end at other corner of house
    return ends
        

def validate_input(d, l):
    """ Throws a ValueError if the given input does not meet the preconditions of
        the problem.

        d -- a list of numbers
        l -- a number
    """
    # d must start at 0.0 and have at least two elements
    if len(d) < 2:
        raise ValueError("Input must have at least 2 points")
    
    if d[0] != 0.0:
        raise ValueError("Input must start at 0")

    # d must be increasing
    if min(d[i] - d[i - 1] for i in range(1, len(d))) <= 0.0:
        raise ValueError("Input must be strictly increasing")

    # l must be positive
    if l <= 0.0:
        raise ValueError("Length of fence segments must be positive")
    
    # d must not have gaps larger than L
    if max(d[i] - d[i - 1] for i in range(1, len(d))) > l:
        raise ValueError("Input has gaps not spannable by fence")

    # find last q such that d[q] <= l
    q = 0
    while q + 1 < len(d) and d[q + 1] <= l:
        q = q + 1

    #print(q)
    #print(d)
    # make sure starting at any tree always covers at least q others
    #print([(d[i], (d[i + q] if i + q < len(d) else (d[(i + q + 1) % len(d)] + d[-1]))) for i in range(len(d) - 1)])
    if sum(1 for i in range(len(d) - 1) if (d[i + q] if i + q < len(d) else (d[(i + q + 1) % len(d)] + d[-1])) - d[i] > l) > 0: 
        raise ValueError("Sparsest section not at beginning of input")

    return


def validate_solution(d, l, solution):
    """ Throws an exception if the given solution is not a valid solution. """
    # check that solution starts with a point < L
    if solution[0] >= l:
        raise ValueError("solution must start with a point < L")

    # check that final point is first point + length of perimeter
    if solution[-1] != solution[0] + d[-1]:
        raise ValueError("solution doesn't end where it starts")
    
    # check that solution is increasing
    if min(solution[i] - solution[i - 1] for i in range(1, len(solution))) <= 0.0:
        raise ValueError("solution must be strictly increasing")

    # check that endpoints in solutions are no more than L apart
    if max(solution[i] - solution[i - 1] for i in range(1, len(solution))) > l:
        raise ValueError("solution requires segment > L")

    # check that solution is a subsequence of d, allowing for wraparound
    points = d[:]
    i = 1
    while i < len(d) and d[i] <= l:
        points.append(d[i] + d[-1])
        i = i + 1

    i = 0
    for x in solution:
        while i < len(points) and points[i] != x:
            i = i + 1
        if i == len(points):
            raise ValueError("invalid point in solition")
    return
    

if __name__ == "__main__":
    main()
