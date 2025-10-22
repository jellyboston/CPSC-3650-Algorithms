def vendor_schedule(n, k, profit, m):
    """ Returns the schedule with the highest net profit given weekly profit
        for each city and given moving cost.  The schedule is returned as a list
        of length n where each element gives the index of the city to vend in
        for the corresponding week.

        n -- an positive integer
        k -- an integer 2 or greater
        profit -- a k-row, n-column array (list of lists) of numbers giving weekly
                  profit for each city --> (city x week)
        m -- a positive number

        Sample Input:
        vendor_schedule(
            n=4 weeks
            k=3 cities
            profit=(3x4) 
            m=2
        )
        returns: 
    """
    '''
    determines whether moving or staying is optimal and
    updates parents in the process
    '''
    def choose_move_stay(diff_city, same_city, best_city, best_count, best_prev, c, w, prev_vals):
        if diff_city >= same_city:
            # move and settle ties if not unique best city
            if best_city == c and best_count == 1:
                prev_city = max((pc for pc in range(k) if pc != c),
                                key=lambda pc: prev_vals[pc])
            else:
                candidates = [pc for pc in range(k) if prev_vals[pc] == best_prev and pc != c] \
                             or [pc for pc in range(k) if prev_vals[pc] == best_prev]
                prev_city = candidates[0]
            trace_parent[c][w] = prev_city
            return diff_city
        else:
            # stay
            trace_parent[c][w] = c
            return same_city

    '''
    recursive function should return an int of the highest profit 
    correspond to the last week 
    '''
    opt = [[None] * n for _ in range(k)] # profit can potentially be neg
    trace_parent = [[None] * n for _ in range(k)]
    def memoized_vendor(w, c):
        if w==0: 
            if opt[c][0] is None:
                opt[c][0] = profit[c][0]
                trace_parent[c][0] = None 
                return opt[c][0]
        if opt[c][w] is not None:
            return opt[c][w]

        # goal: precompute moves from all prev c' to this c
        prev_vals = [memoized_vendor(w-1, c2) for c2 in range(k)]

        # compute previous week's profit of the same city
        same_city = prev_vals[c]

        # account for first/second best values
        best_prev, next_best_prev = float('-inf'), float('-inf')
        best_city, best_count = -1, 0
        for city_idx, value in enumerate(prev_vals):
            if value > best_prev:
                next_best_prev = best_prev
                best_prev, best_city, best_count = value, city_idx, 1
            elif value == best_prev:
                # NOTE: we need to keep track of best city ties
                best_count += 1
            elif value > next_best_prev:
                next_best_prev = value
        
        # compute the best previous week's profit traveling from a different city
        diff_city = (next_best_prev if (best_city == c and best_count == 1) else best_prev) - m # if unique
        move = choose_move_stay(diff_city, same_city, best_city, best_count, best_prev, c, w, prev_vals)
        opt[c][w] = profit[c][w] + move
        return opt[c][w]
    
    # YOUR SOLUTION HERE
    opt_vals = [memoized_vendor(n-1, city) for city in range(k)]
    end_city = max(range(k), key=lambda c: opt_vals[c])

    # backtrace
    schedule = [None] * n
    curr = end_city
    for week in range(n-1, -1, -1):
        schedule[week] = curr
        curr = trace_parent[curr][week]
    return schedule 