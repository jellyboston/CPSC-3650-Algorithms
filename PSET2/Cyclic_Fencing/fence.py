'''
Runtime: theta(n)
Tasks: Explain why its worst-case runtime is theta(n)
Explanation:
In Phase A, we compute an extended array of fence points in Θ(n) time. We skip d[0] + P,
so at most n-1 shifted trees are appened and the extended array has size O(n).

In Phase B, we then utilize a sliding window strategy to pre-compute
the farthest pt that satisfies the pre-condition (extend[r] - extend[i] ≤ L) 
in order to avoid repeated work.
The farthest[] array is built in O(n) because the right pointer only advances---it
never resets as in the brute force case. r moves forward at most n steps, i moves n steps,
so O(n) total. 

In Phase C, the greedy algorithm only tries starts with value < L as required by the spec. 
We enforce that the last output = first + P to represent a full loop

The farthest[] array allows each greedy step to be as simple as an array index operation, 
which is a constant-time jump of O(1) per step, so the runtime for a single start 
equals the number of segmentsfrom that start.

In the worst case, there are Θ(n) starts and each path has O(n) segments, but due to the 
precompute we can bound the overall work to Θ(n) since we never re-scan segments across
these starts.

Thus, the runtime of optimize_fence() can be shown as theta(n).
'''

def optimize_fence(d, l):
    # build wrap around array
    # PHASE A
    perimeter = d[-1]
    extend = d[:]
    i = 1
    while extend[-1] < perimeter + l and i < len(d):
        extend.append(perimeter + d[i])
        i += 1

    # PHASE B (sliding window technique)
    r= 0
    farthest = [None] * len(extend) # farthest[i] is a pt as far as possible w/o exceeding l
    for i in range(len(extend)):
        # guard right pointer 
        if r < i:
            r = i
        while r + 1 < len(extend) and extend[r+1] - extend[i] <= l:
            r += 1
        farthest[i] = r

    # PHASE C greedy algorithm: pick min segments
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