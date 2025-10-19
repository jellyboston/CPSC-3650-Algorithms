def find_lcs(s1, s2, l):
    """ Finds the longest common subsequence of s1 and s2 given the length
        of the longest common subsequences of all combinations of their
        prefixes.

        s1 -- a string
        s2 -- a string
        l -- a 2-D array (list of lists) where l[i][j] gives the length of the
             longest common subsequence of s1[:i] and s2[:j] (the first i and first j
             characters of s1 and s2 respectively)

        ex: lcs("stone", "longest", l)
            returns "one"
    """
    # YOUR SOLUTION HERE
    # already given the subsequence table, so trace top down
    def backtrace_lcs(result, curr_row, curr_col):
        while curr_row > 0 and curr_col > 0 and l[curr_row][curr_col] != 0:
            # check value of left and above
            left = l[curr_row][curr_col - 1] if curr_col > 0 else -1
            above = l[curr_row - 1][curr_col] if curr_row > 0 else -1
            if l[curr_row][curr_col] == left:
                # move back and update position to left idx
                curr_col = curr_col - 1
            elif l[curr_row][curr_col] == above:
                curr_row = curr_row - 1
            else:
                # left and above don't match -> traverse diagonal
                assert s1[curr_row - 1] == s2[curr_col - 1]
                result.append(s1[curr_row - 1])
                curr_row, curr_col = curr_row - 1, curr_col - 1
        return result

    result = []
    # start from bottom right of l
    curr_row, curr_col = len(s1), len(s2)  # since init table size is len() + 1
    chars = backtrace_lcs(result, curr_row, curr_col)
    # we appended while walking backwards, so reverse to restore forward order
    return ''.join(reversed(chars))