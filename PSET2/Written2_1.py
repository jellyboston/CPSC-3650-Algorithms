def consecutive_helper(A, i, last, count, total):
    """ 
    Postcondition: On return, the function holds true if and only if there is a
    consecutive run of 'total' equivalent integers for A[i:]. If count > 0, then this run
    must begin at A[i] and continue for the next 'count' positions with value equal
    to 'last'. Otherwise, the run may start later in A[i:].

    A -- a list of numbers for the array to search
    i -- an integer in 0, ..., len(A) for the current position in the array
    last -- a number for the value to look for in A[i]
    count -- a nonnegative integer for the number of occurrences of last
    to look for starting at A[i]
    total -- a positive integer greater than count for the number of occurrences
    of something else to look for
    """
    if count == 0:
        # looking for 0 more lasts in a row
        return True
    elif i == len(A):
        # out of places to look and didn't find anything
        return False
    elif A[i] == last:
        # found one more value equal to last
        return consecutive_helper(A, i + 1, last, count - 1, total)
    else:
        # starting a new run; look for total-1 to follow
        return consecutive_helper(A, i + 1, A[i], total - 1, total)
    
    '''
    Proceed by weak induction. Let k represent n - i, the length of the remaining input
    in array A. Let P(k) represent the inductive hypothesis and denote:

    For any call to consecutive_helper() on a suffix A[i:] of length k, 
    the function returns True if and only if there is a
    consecutive run of 'total' equal integers for A[i:]. If count > 0, then this run
    must begin at A[i] and continue for the next 'count' positions with value equal
    to 'last'. Otherwise, the run may start later in A[i:].

    Base Case: If k=0, then i == len(A). By definition, this means that the suffix of A[i:]
    is empty and that no run of length 'total' exists, and the function returns False. This
    matches the postcondition/IH.

    Base Case: If count == 0, then it must be that the 'total' number of consecutive equal 
    integers has been found, and the function returns True. This also matches the IH.

    Inductive Case: We will show that P(k) => P(k+1). Suppose that a consecutive suffix
    exists in this run. If A[i] == last, a recursive call is made to check the next index
    corresponding to k + 1 with count deceremented. By the inductive hypothesis and our assumption
    that a consecutive suffix exists, the next step will also decrement the count and proceed.

    Inductive Case: We will show that P(k) => P(k+1). Suppose that we have a suffix A[i:] of
    length k + 1. If A[i] == last, then a recursive call will be made for A[i+1:] with
    suffix length k and count decremented. By the inductive hypothesis, the postcondition
    holds for this next call. Therefore, the postcondition must also hold true for P(k+1)
    since the current element extends the run correctly under the IH. 

    In the else case, suppose we again have suffix A[i:] of length k+1. By the logic
    of consecutive_helper(), it must be true that count is not 0 and the array traversal
    is not finished. Thus, a recursive call will be made for A[i+1:] with total-1 remaining, which correctly
    begins a new run from this point. By the inductive hypothesis, the postcondition holds for this smaller
    suffix P(k+1), and therefore it also holds for A[i:].

    Thus, by weak induction, consecutive_helper() satisfies the postcondtion for all inputs.
    '''

    