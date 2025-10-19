import sys

import rod

def main():
    m = int(sys.stdin.readline())
    price = [0] + [int(s) for s in sys.stdin.readline().split()]

    if m < 0.0:
        raise ValueError(f"cut cost must be nonnegative; was {m}")
    if len(price) < 2:
        raise ValueError("must give rod prices for at least length 1")
    if (sum(1 for p in price if p < 0.0) > 0):
        raise ValueError("all prices must be nonnegatove")
    
    print(rod.cut_rod(len(price) - 1, price, m))
    

if __name__ == "__main__":
    main()
    
