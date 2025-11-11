import sys
import random
import itertools as it

from flow_graph import FlowGraph
import update

def read_graph():
    # read number of vertices
    n = int(sys.stdin.readline())
    if n <= 0:
        raise ValueError(f"Invalid number of vertices: {n}")
    g = FlowGraph(n)
    source = 0
    sink = n - 1

    # read one edge per line
    for line in sys.stdin:
        ends = line.split()
        if len(ends) == 0:
            break
        if len(ends) != 4:
            raise ValueError(f"Invalid edge: {line}")
        u = int(ends[0])
        v = int(ends[1])
        c = int(ends[2])
        c_r = int(ends[3])
        if u < 0 or u >= n:
            raise ValueError(f"Invalid from index: {u}")
        if u == sink:
            raise ValueError(f"Edge from sink to {v}")
        if v < 0 or v >= n:
            raise ValueError(f"Invalid to index: {v}")
        if v == source:
            raise ValueError(f"Edge from {u} to source")
        if c < 0:
            raise ValueError(f"negative capacity {c} for ({u}, {v})")
        if c_r < 0:
            raise ValueError(f"negative capacity {c_r} for ({u}, {v}) reversed")
        if c + c_r == 0:
            raise ValueError(f"zero total capacity {c_r} between ({u}, {v})")
        # given capacity in the given direction, 0 in the other
        g.add_edge(u, v, c, c_r)
    return g


def main():
    g = read_graph()
    n = g.size()
    source = 0
    sink = g.size() - 1
    
    # read number of augmenting paths
    path_count = int(sys.stdin.readline())

    # read, validate, and update flow along each path
    for i in range(path_count):
        verts = [int(v) for v in sys.stdin.readline().split()]

        if len(verts) < 2:
            raise ValueError(f"path {verts} too short")
        
        if verts[0] != source:
            raise ValueError(f"path must start at source {source}, not {verts[0]}")

        if verts[-1] != sink:
            raise ValueError(f"path must end at sink {sink}, not {verts[-1]}")
        
        path = []
        for j in range(len(verts) - 1):
            u = verts[j]
            v = verts[j + 1]
            if u < 0 or u >= n:
                raise ValueError(f"invalid vertex {u} in path {verts}")
            if v < 0 or v >= n:
                raise ValueError(f"invalid vertex {v} in path {verts}")
                
            e = g.find_edge(u, v)
            if e is None:
                raise ValueError(f"no edge between {u} and {v}")

            path.append(e)

        # get residual capacity of bottleneck edge
        b = min(e.residual() for e in path)

        if b == 0:
            raise ValueError(f"path {verts} has no residual capacity")

        # update flow and residual capacity along path
        for e in path:
            update.update(e, e.opposite(), b)

        # ensure capacity, conservation, and one-way flow all satisfied
        g.validate(source, sink)
    
    # print(g)
    g.validate(source, sink)
    print(g.value(source))

    
if __name__ == "__main__":
    main()
