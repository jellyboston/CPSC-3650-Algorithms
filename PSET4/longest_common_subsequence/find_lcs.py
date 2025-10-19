import sys
import lcs

def len_lcs(s1, s2):
    """ Finds the length of the longest common subsequences of all
        prefixes of s1 and s2.  The return value is a 2-D array (list of
        lists) so that the element at row i, column j is the length of
        the longest common subsequence of s1[:i] and s2[:j].  The length
        of the longest common subsequence of i and j is then in row
        len(s1), column len(s2).

        s1 -- a string
        s2 -- a string
    """
    # initialize table to all 0's
    # (covers the base case of l[i,0]=l[0,j]=0
    l = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # fill table top-to-bottom, left-to-right
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                l[i + 1][j + 1] = 1 + l[i][j]
            else:
                l[i + 1][j + 1] = max(l[i][j + 1], l[i + 1][j])

    return l


def is_subsequence(sub, s):
    """ Determines if the first string is a subsequence of the second.  Returns
        true if so and false otherwise.

        sub -- a string
        s -- a string (>= sub)
    """
    matches = 0
    i = 0
    m = len(sub)
    n = len(s)
    while matches < m and i < n:
        if sub[matches] == s[i]:
            matches += 1
        i += 1
    return matches == m
    

if __name__ == "__main__":
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()

    l = len_lcs(s1, s2)

    lcs = lcs.find_lcs(s1, s2, l)

    if is_subsequence(lcs, s1) and is_subsequence(lcs, s2):
        print(len(lcs))
    else:
        print(f"{lcs} is not a common subsequence of {s1} and {s2}")
