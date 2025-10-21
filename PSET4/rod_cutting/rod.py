from functools import lru_cache

def cut_rod(n, price, m):
    """ Returns the maximum value after cutting a rod of length n, given
        the price of rod segments and the cost of a cut.  Assumes cuts can't
        leave less than 1 at each end and that 1 unit is wasted per cut.

        n -- a positive integer the the length of the rod to cut
        price -- a list of n+1 nonnegative numbers for the price of rod lengths from 0 through n
        m -- a nonnegative number for the cost per cut

        returns -- max value

        reccurence: l[i] = 0 if n = 0, 
                           max(price[n], price[c] + v(n-c-1) - m) else
    """
    # YOUR SOLUTION HERE
    values = [0] * (n+1)

    # begin by solving base subproblems
    for i in range(1, n+1):
        # values[i] = float('-inf')
        values[i] = price[i]
        for c in range(1, i-1): # must account for 1 at the edges (constraint)
            # 1 unit wasted per cut (constraint)
            remaining_cut = i - c - 1 
            if remaining_cut < 0: continue
            # subtract cost (constraint)
            subproblem = price[c] + values[remaining_cut] - m
            if subproblem > values[i]: 
                values[i] = subproblem
    return values[n]

'''
Experimental implementation using memoization. A friend
showed me how to use the lru_cache decorator and now im obsessed.

Timing analysis:
DP approach:
0.14590555988252163
LRU cache:
0.22687724977731705

Results:
- in python, DP approach is useually more efficient (LRU has to setup cache decorator wrapping,
recursive stack creations and function calls)
- but in Java/C apparently they should both tie 
'''
def cut_rod_experiment_memoization(n, price, m):
    @lru_cache(maxsize=None)
    def best_value(i):
        if i <= 0:
            return 0
        value_i = price[i]
        for c in range(1, i - 1):
            remaining_cut = i - c - 1
            if remaining_cut < 0: continue
            sub = price[c] + best_value(remaining_cut) - m
            if sub > value_i:
                value_i = sub
        return value_i
    return best_value(n)