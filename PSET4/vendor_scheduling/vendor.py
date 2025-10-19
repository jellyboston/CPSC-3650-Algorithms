import sys

import schedule

def main():
    n = int(sys.stdin.readline())
    if n <= 0:
        raise ValueError(f"number of weeks must be positive; got {n}")
    
    k = int(sys.stdin.readline())
    if k <= 1:
        raise ValueError(f"must have at least 2 cities; got {k}")

    m = float(sys.stdin.readline())
    if m <= 0.0:
        raise ValueError(f"moving cost must be nonnegative; got {m}")
    
    profit = []
    for c in range(k):
        row = [float(s) for s in sys.stdin.readline().split()]
        if len(row) != n:
            raise ValueError(f"must have profit in every week for city {c}")
        profit.append(row)

    sched = schedule.vendor_schedule(n, k, profit, m)

    if len(sched) != n:
        raise ValueError(f"schedule should be of length {n}; got {sched}")
    
    total = 0
    for w in range(n):
        if sched[w] < 0 or sched[w] >= k:
            raise ValueError(f"invalid city {sched[n]} in schedule")
        total += profit[sched[w]][w]
        if w > 0 and sched[w] != sched[w - 1]:
            total -= m

    print(total)
    

if __name__ == "__main__":
    main()
    
