## 2.4
**Preconditions:**
* loc is a list of distances from the starting point
* The first element is 0.0
* No two consecutive elements will have a difference of more than max_d 
* `max_d` > 0
* `max_e` >= 0

**Counter-example:**
```python
# Input
# The following are consistent with the preconditions 
loc = [0, 1, 2, 3, 4, 4.5, 5.5, 6]
max_d = 1.0
max_e = 1.0

# Output from schedule_travel()
stop_points = [2, 3, 4, 5, 6, 7] # len() = 6

# One Optimal Schedule
stop_points_optimized = [1, 2, 3, 5, 7] # len() = 5
```

The intuition here is that we can exploit the greedy choice used by `schedule_travel()` to
front load stamina usage early in the loop, which will lead to a suboptimal schedule. The
`max_e` constraint is what breaks the greedy approach here, else the problem would be similar
to the fencing algorithm. 
