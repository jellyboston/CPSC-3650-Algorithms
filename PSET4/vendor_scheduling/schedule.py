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
    # YOUR SOLUTION HERE
    '''
    recursive function should return an int of the highest profit 
    correspond to the last week 
    '''
    opt = [[None] * n for _ in range(k)] # profit can potentially be neg
    def memoized_vendor(w, c):
        if w==0: 
            opt[c][0] = profit[c][0]
            return profit[c][0]
        if opt[c][w] is not None:
            return opt[c][w]

        # goal: precompute moves from all prev c' to this c
        prev_vals = [memoized_vendor(w-1, c2) for c2 in range(k)]

        # compute previous week's profit of the same city
        same_city = prev_vals[c]

        # account for first/second best values
        best_prev, next_best_prev = float('-inf'), float('-inf')
        best_city = -1
        for city_idx, value in enumerate(prev_vals):
            if prev_vals[city_idx] > best_prev:
                next_best_prev = best_prev
                best_prev = value
                best_city = city_idx
            elif prev_vals[city_idx] > next_best_prev:
                next_best_prev = value
        
        # compute the best previous week's profit traveling from a different city
        diff_city = (next_best_prev if best_city == c else best_prev) - m
        opt[c][w] = profit[c][w] + max(diff_city, same_city)
        return opt[c][w]
    
    max_opt_profit = memoized_vendor(n, k)
    # backtrace



    return 

'''
    for w in range(n):
        for c in range(k):
            if w==0: memo[c][0] = profit[c][0]
            # compute the subproblem

'''