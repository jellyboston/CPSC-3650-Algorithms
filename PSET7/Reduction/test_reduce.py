import sys
import random
import itertools as it

from graph import Graph
import reduction


def read_graph():
    # read and check number of vertices
    n = int(sys.stdin.readline())
    g = Graph(n)

    # read one edge per line
    for line in sys.stdin:
        ends = line.split()
        if len(ends) != 2:
            raise ValueError(f"Invalid edge: {line}")
        u = int(ends[0])
        v = int(ends[1])
        if u < 0 or u >= n:
            raise ValueError(f"Invalid vertex index: {u}")
        if v < 0 or v >= n:
            raise ValueError(f"Invalid vertex index: {v}")
        g.add_edge(u, v)
    return g


def check_appxHP(g):
    """ Given a graph G return True if G satisfies approximate HP,
        otherwise return False

        g -- a graph
    """
    def has_approx_hp(g, curr, repeat, on_path, from_repeat, total, n):
        """ Determines if the path taken to this recursive call can be
            extended to an approx-HP that repeats the given vertex.

            g -- an undirected graph
            curr -- the index of the vertex at the end of the current path
            repeat -- the index of the vertex allowed to repeat
            on_path -- the number of times each vertex appears on the current path
            from_repeat -- whether an edge from repeat appear on path
            total -- the total number of unique vertices on the path
            n -- the number of vertices in g
        """
        if total == n:
            return True

        # go over outgoing edges from current vertex
        for v in g.edges(curr):
            # can go to unseen or repeatable vertex
            if on_path[v] == 0 or (v == repeat and not from_repeat[curr]):
                # track vertices and edges used
                new_total = (total + 1) if on_path[v] == 0 else total
                on_path[v] += 1
                if curr == repeat:
                    from_repeat[v] = True
                elif v == repeat:
                    from_repeat[curr] = True
                    
                if has_approx_hp(g, v, repeat, on_path, from_repeat, new_total, n):
                    return True

                # undo path tracking
                on_path[v] -= 1
                if curr == repeat:
                    from_repeat[v] = False
                elif v == repeat:
                    from_repeat[curr] = False
        return False
        
    n = g.size()
    
    # for each possible starting vertex and repeated vertex
    # check for approx-HP by backtracking
    
    # on_path[v] is the number of times v is on the current path
    on_path = [0] * n
    
    # from_repeat[v] is whether the edge (repeat, v) is on the path
    from_repeat = [False] * n
    
    for start in range(n):
        for repeat in range(n):
            on_path[start] = 1
            if has_approx_hp(g, start, repeat, on_path, from_repeat, 1, n):
                return True
            on_path[start] = 0
    return False
    

def main():
    g = read_graph()
    
    # check wheel-ness
    gr = reduction.reduce(g)
    print(check_appxHP(gr))


if __name__ == "__main__":
    main()
