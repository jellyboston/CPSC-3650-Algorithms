import sys

from digraph import Digraph
import scc


def read_digraph():
    # read and check number of vertices
    n = int(sys.stdin.readline())
    if n <= 0:
        raise ValueError(f"Invalid number of vertices: {n}")
    g = Digraph(n)

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


def find_part(n, partition):
    """ Returns a list so that index i of the returned list gives the index of the
        part of the partition that contains i.
        n -- a positive integer
        partition -- a list of lists that partition {0, ..., n-1}
    """
    part_containing = [None] * n # the index of the SCC each vertex belongs to
    for i, part in enumerate(partition):
        for j in part:
            part_containing[j] = i
    return part_containing


def normalize_within_sccs(n, sccs):
    """ Reorders SCCs in the given list of SCCs, where each SCC is given as a list
        of indices of vertices in the SCC in no particular order.  In the output, the
        vertices in each SCC will be listed in increasing order.

        n -- a nonnegative integer
        sccs -- a list of lists, where the inner lists partition [0, ..., n-1]
    """
    # determine index of SCC each vertex belongs to
    scc_containing = find_part(n, sccs)

    # create reorganized list by going through vertices in increasing order
    result = [[] for i in range(len(sccs))] # create initially empty list of SCCs
    for v in range(n):
        result[scc_containing[v]].append(v)

    return result


def normalize_between_sccs(n, sccs):
    """ Reorders the given list of SCCs so the SCCs appear in order of increasing
        minimum vertex index.

        n -- a nonnegative integer
        sccs -- a list of lists, where the inner lists partition [0, ..., n-1]
                and are in increasing order
    """
    scc_containing = find_part(n, sccs)
    
    # find minimum vertex in each scc
    min_vert = [scc[0] for scc in sccs]

    # scc_order will give, for the representative (minimum) vertex in each SCC, the index of the SCC
    scc_order = [None] * n
    for v in min_vert:
        scc_order[v] = scc_containing[v]

    # copy SCCs from original list in order they appear in scc_order
    result = []
    for i in range(n):
        if scc_order[i] is not None:
            result.append(sccs[scc_order[i]])
        
    return result


def main():
    g = read_digraph()
    print(normalize_within_sccs(g.size(), scc.sccs(g)))

    
if __name__ == "__main__":
    main()
