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
            remaining_cut = i - c - 1 # 1 unit wasted per cut (constraint)
            if price[c] + values[remaining_cut] > values[i]:
                values[i] = price[c] + values[remaining_cut]
    return values[n]
