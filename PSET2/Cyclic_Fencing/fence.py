'''
First step - OH Questions:
1. Clarify the problem -- what does L represent?
2. Brainstorm the bruteforce approach

Constraints:
1. 

Runtime: theta(n)

Input: 

Output: 

Tasks: explain why its worst-case runtime is theta(n)
'''

def optimize_fence(d, l):
    # YOUR SOLUTION HERE
    # build wrap around array
    perimeter = d[-1]
    extend = d[:]
    i = 1
    while extend[-1] < perimeter + l and i is not len(d):
        extend.append(perimeter + d[i])
        i += 1
    '''
    Pre-compute technique: apply dynamic sliding window (two pointers)
    - farther[i] represents the maximal valid index for this i (while <= l)
    '''
    r= 0
    farthest = [None] * len(extend) # farthest[i] is a pt as far as possible w/o exceeding l
    for i in range(len(extend)):
        # guard right pointer 
        if r < i:
            r = i
        while r + 1 < len(extend) and extend[r+1] - extend[i] <= l:
            r += 1
        farthest[i] = r

    # greedy algorithm: pick min segments
    best_count = None
    best_output = None
    start = 0
    while d[start] < l:
        i = start
        target = extend[start] + perimeter
        seg_count = 0
        path = []
        while extend[i] < target:
            path.append(extend[i])
            i = farthest[i]
            seg_count += 1
        path.append(target)
        if best_count is None or seg_count < best_count:
            best_count = seg_count
            best_output = path
        start += 1
    return best_output